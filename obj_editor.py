import bpy
import os
import math
from mathutils import Vector

import data_generator

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
def degreeToEuler(degree):
    return (degree * 2 * math.pi) / 360

def GetObjectAndUVMap(objName, uvMapName):
    '''
    UVMap을 가져오는 함수
    :param objName: object 이름
    :param uvMapName: uvmap 이름
    :return: 입력값을 갖고 있는 obj, uvmap
    '''
    try:
        obj = bpy.data.objects[objName]
        if obj.type == 'MESH':
            uvMap = obj.data.uv_layers[uvMapName]
            return obj, uvMap
    except:
        pass
    return None, None


# Scale a 2D vector v, considering a scale s and a pivot point p


def Scale2D(v, s, p):
    '''
    변환된 uvmap 반환(index단위 계산)
    :param v: uvmap 내부 데이터(index값)
    :param s: scale
    :param p: pivot
    :return: 스케일 조정 완료된  uvmap index
    '''
    return (p[0] + s[0] * (v[0] - p[0]), p[1] + s[1] * (v[1] - p[1]))


# Scale a UV map iterating over its coordinates to a given scale and with a pivot point

def ScaleUV(uvMap, scale, pivot):
    '''
    uvmap scale 조정 함수
    :param uvMap: 조정할 uvmap
    :param scale: Scale
    :param pivot: pivot
    :return: 스케일 조정 완료된  uvmap
    '''
    for uvIndex in range(len(uvMap.data)):
        uvMap.data[uvIndex].uv = Scale2D(uvMap.data[uvIndex].uv, scale, pivot)


def makeTexture(ob, imagePath):
    '''
    object에 image texture 입히는 함수
    :param ob: object
    :param imagePath:texture image
    '''
    # Get material

    mat = bpy.data.materials.get("Material")
    mesh=bpy.data
    dup=bpy.data.objects.new(ob.name,mesh.copy())
    dup.active_material=mat.copy()


    # if mat is None:
    #     # create material
    #     mat = bpy.data.materials.new(name="Material")
    #
    # # Assign it to object
    #
    # if ob.data.materials:
    #     # assign to 1st material slot
    #
    #     bsdf = mat.node_tree.nodes["Principled BSDF"]
    #     texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    #     texImage.image = bpy.data.images.load(imagePath)
    #     texImage.location = 0, 0
    #     mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    #        bpy.ops.uv.smart_project(angle_limit=0, island_margin=0.00, user_area_weight=0.0)
    #     cyluvs = ob.data.uv_layers[0].data

def makeJointResize(savepath, inputFile, insertimage, newSize, diameter,fid,jobid):
    '''
    연결부 길이 조정
    :param savepath: 저장될 파일 위치
    :param inputFile: 기본 모델링 파일(full path, obj pipe file)
    :param insertimage: texture로 입힐 이미지 파일(필수아님)
    :param newSize: 새로 만들어질 연결부의 길이(단위 : m) 0이면 원래 길이대로
    :param diameter: 새로 만들어질 연결부 직경(단위 : m)
    :param fid: 요청한 fid
    :param jobid: 요청한  jobid
    '''
    objFileName = inputFile.split('\\')[len(inputFile.split('\\')) - 1]
    file_loc = inputFile
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    scene = bpy.context.scene
    obs = []
    for ob in scene.objects:
        if ob.type == 'MESH':
            obs.append(ob)
    ctx = bpy.context.copy()
    # one of the objects to join
    ctx['active_object'] = obs[0]

    ctx['selected_objects'] = obs
    # In Blender 2.8x this needs to be the following instead:
    # ctx['selected_editable_objects'] = obs

    bpy.ops.object.join(ctx)
    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    strm = inputFile.split('joint-')[1].split('mm')[0]
    flm = float(strm)
    objName = bpy.data.objects[0].name
    uvMapNAme = 'UVMap'
    pivot = Vector((0.5, 0.5))
    scale = Vector((1, 1))
    obj, uvMap = GetObjectAndUVMap(objName, uvMapNAme)
    if obj is not None:
        ScaleUV(uvMap, scale, pivot)
    if newSize==0:
        obj_object.scale.x = (diameter / flm)
        obj_object.scale.y = (diameter / flm)
        obj_object.scale.z = 1
    else:
        obj_object.scale.x = (diameter/flm )
        obj_object.scale.y = (diameter /flm)
        obj_object.scale.z = 1
    if insertimage != None:
        if os.path.isfile(insertimage):  # isfile
            makeTexture(obj_object, insertimage)
    directory = savepath + '\\' + jobid + '\joint\\'
    directory_replaced = directory.replace('\\', '/', 10)
    createFolder(directory_replaced)
    bpy.ops.export_scene.obj(
        filepath=directory_replaced + fid + ".obj")
    bpy.ops.object.delete()
    return directory_replaced + fid + ".obj"

def makePipeResize(savepath, inputFile, insertimage, inputWidth, newSize, newWidth,jobid):
    '''
    직관 파이프 길이조정
    :param savepath: 저장될 파일 위치
    :param inputFile: 기본 모델링 파일(full path, obj pipe file)
    :param insertimage: texture로 입힐 이미지 파일(필수아님)
    :param inputWidth: inputFile 파이프의 직경 (단위 : cm)
    :param newSize: 새로 만들어질 파이프의 길이 (단위 : cm)
    :param newWidth: 새로 만들어질 파이프 직경 (단위 : cm)
    :param fid: 요청한 fid
    :param jobid: 요청한  jobid
    '''
    bpy.ops.object.delete()
    objFileName = inputFile.split('\\')[len(inputFile.split('\\')) - 1]
    file_loc = inputFile
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    strm = inputFile.split('pipe-')[1].split('m')[0]
    flm = float(strm)
    objName = bpy.data.objects[0].name
    # uvMapNAme = 'UVMap'
    # pivot = Vector((0.5, 0.5))
    # scale = Vector((newSize / flm, 1))
    # obj, uvMap = GetObjectAndUVMap(objName, uvMapNAme)
    # if obj is not None:
    #     ScaleUV(uvMap, scale, pivot)
    obj_object.scale.x = (newWidth/ inputWidth)
    obj_object.scale.y = (newWidth/inputWidth)
    obj_object.scale.z = (newSize/flm)
    if insertimage != None:
        if os.path.isfile(insertimage):  # isfile
            makeTexture(obj_object, insertimage)
    directory=savepath + '\\'+jobid+'\pipe\\'
    directory_replaced=directory.replace('\\','/',10)
    createFolder(directory_replaced)
    bpy.ops.export_scene.obj(
        filepath=directory_replaced+"pipe-"+str(newSize)+".obj")
    bpy.ops.object.delete()
    return directory_replaced+"pipe-"+str(newSize)+".obj"

def makeHoleCResize(savepath, diameter, length, corver_width,cover_diameter, insertImage,inputFile,fid,jobid):
    '''
    m원형맨홀
    :param savepath:저장할 위치
    :param diameter: 맨홀 직경
    :param length: 맨홀 길이
    :param corver_width:뚜껑 넓이
    :param cover_diameter: 뚜껑직경
    :param insertImage: 뚜껑 입힐 이미지
    :param fid:
    :param jobid:
    :return:
    '''
    coverFile = os.path.join(savepath , 'hole' , str(corver_width) +"x"+str(cover_diameter) , str(int(cover_diameter)) +"_hole.obj")
    if os.path.exists(coverFile)!=True:
        coverFile=inputFile
    file_loc = coverFile
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    obj_object.scale.x = 1
    obj_object.scale.y = 1
    obj_object.scale.z = 1
    obj_object.location = (0, 0, (length) * -1)
    if insertImage != None:
        if os.path.isfile(insertImage):  # isfile
            makeTexture(obj_object, insertImage)
    bpy.ops.mesh.primitive_cylinder_add(radius=(diameter / 1000) / 2, depth=(length),
                                        location=(0, 0, ((length) / 2) * -1))
    directory = savepath + '\\' + jobid + '\hole\C\\'
    directory_replaced = directory.replace('\\', '/', 10)
    createFolder(directory_replaced)
    bpy.ops.export_scene.obj(
        filepath=directory_replaced + fid + ".obj")
    objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA', 'MESH')]
    bpy.ops.object.delete({"selected_objects": objs})
    return directory_replaced + fid + ".obj"

def makeHoleSResize(savepath,width,height,hole_depth,cover_diameter, insertImage,inputFile,fid,jobid):
    '''
    사각 맨홀 사이즈 조절
    :param savepath: 저장될 파일 위치
    :param height: 맨홀높이
    :param hole_depth: 맨홀길이
    :param width: 뚜껑넓이
    :param cover_diameter: 뚜껑직경
    :param insertImage: texture로 입힐 이미지 파일
    :param inputFile: 파일 못찾았을 때 대신할 뚜껑파일
    '''
    coverFile = os.path.join(savepath,'hole',str(int(width))+"x"+str(int(height))+"x"+str(int(cover_diameter)),str(int(cover_diameter))+ "mm_hole.obj")
    if os.path.exists(coverFile)!=True:
        coverFile=inputFile
    file_loc = coverFile
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    obj_object.scale.x = 1
    obj_object.scale.y = 1
    obj_object.scale.z = 1
    obj_object.location = (0, 0, (hole_depth) * -1)
    if insertImage != None:
        if os.path.isfile(insertImage):  # isfile
            makeTexture(obj_object, insertImage)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, ((hole_depth) / 2) * -1))
    bpy.ops.transform.resize(value=(width/1000, height/1000, hole_depth))
    directory = savepath + '\\' + jobid + '\hole\S\\'
    directory_replaced = directory.replace('\\', '/', 10)
    createFolder(directory_replaced)
    bpy.ops.export_scene.obj(
        filepath=directory_replaced + fid + ".obj")
    objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA', 'MESH')]
    bpy.ops.object.delete({"selected_objects": objs})
    return directory_replaced + fid + ".obj"
def pipeResize(inputFile, insertimage, newSize):
    '''
    기본 모델링 된 파이프 obj를 곡관 만드는 사이즈로 다시 만드는 함수
    :param inputFile: 기본 모델링 된 파이프 obj full path
    :param insertimage: inputFile texture image
    :param newSize: new length
    :return: obj object
    '''
    objFileName = inputFile.split('\\')[len(inputFile.split('\\')) - 1]
    directory_replaced = inputFile.replace('\\', '/', 10)
    file_loc = directory_replaced
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    strm = inputFile.split('pipe-')[1].split('m')[0]
    flm = float(strm)
    objName = bpy.data.objects[0].name
    uvMapNAme = 'UVMap'
    pivot = Vector((0.5, 0.5))
    scale = Vector((newSize / (flm), 1))
    obj, uvMap = GetObjectAndUVMap(objName, uvMapNAme)
    if obj is not None:
        ScaleUV(uvMap, scale, pivot)
    obj_object.scale.x = 1
    obj_object.scale.y = 1
    if newSize=="":
        obj_object.scale.z=1
    else:
        obj_object.scale.z = (newSize / flm)
    if insertimage != None:
        if os.path.isfile(insertimage):  # isfile
            makeTexture(obj_object, insertimage)
    return obj_object
def createCurve(savePath, frontPipeLocation, curveLocation, inputFile, insertImage, roll, fid, jobid):
    '''
    create curve
    :param savePath: save full path
    :param frontPipeLocation: 생성될 곡관 앞 파이프 위치[x,y,z]
    :param curveLocation: 생성될 곡관 위치[x,y,z]
    :param inputFile: 곡관 생성할 때 사용할 파이프 모델링 obj파일
    :param insertImage: input file texture image
    :param roll: 곡관의 각도(degree)
    :param fid:fid
    :param jobid: jobid
    :return: export file name
    '''
    length = round(abs(curveLocation[0] - frontPipeLocation[0]), 1)
    obj_object = pipeResize(inputFile, insertImage, length * 2)
    obj_object.rotation_euler[0] = degreeToEuler(0)
    obj_object.rotation_euler[1] = degreeToEuler(0)
    obj_object.rotation_euler[2] = degreeToEuler(0)
    obj_object2 = pipeResize(inputFile, insertImage, length * 2)
    obj_object2.rotation_euler[0] = degreeToEuler(0)
    obj_object2.rotation_euler[1] = degreeToEuler(roll)
    obj_object2.rotation_euler[2] = degreeToEuler(0)
    bpy.ops.mesh.primitive_cube_add(size=2)
    bpy.context.object.rotation_euler[0] = degreeToEuler(0)
    bpy.context.object.rotation_euler[1] = degreeToEuler(roll / 2)
    bpy.context.object.rotation_euler[2] = degreeToEuler(0)
    bpy.ops.transform.translate(value=(-0.2, 0, -1))
    obj_object.select_set(True)
    bpy.context.view_layer.objects.active = obj_object
    boolean_mod = obj_object.modifiers.new(type="BOOLEAN", name="Boolean")
    boolean_mod.object = bpy.data.objects["Cube"]
    boolean_mod.operation = 'DIFFERENCE'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=boolean_mod.name)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["Cube"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects["Cube"]
    bpy.ops.object.delete(use_global=True)
    bpy.ops.mesh.primitive_cube_add(size=2)
    bpy.context.object.rotation_euler[0] = degreeToEuler(0)
    bpy.context.object.rotation_euler[1] = degreeToEuler(roll / 2)
    bpy.context.object.rotation_euler[2] = degreeToEuler(0)
    bpy.ops.transform.translate(value=(0.2, 0, 1))
    obj_object2.select_set(True)
    bpy.context.view_layer.objects.active = obj_object2
    boolean_mod = obj_object2.modifiers.new(type="BOOLEAN", name="Boolean")
    boolean_mod.object = bpy.data.objects["Cube"]
    boolean_mod.operation = 'DIFFERENCE'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=boolean_mod.name)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["Cube"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects["Cube"]
    bpy.ops.object.delete(use_global=True)
    directory = savePath + '\\' + jobid + '\curve\\'
    directory_replaced = directory.replace('\\', '/', 10)
    createFolder(directory_replaced)
    bpy.ops.export_scene.obj(
        filepath=directory_replaced + fid + ".obj")
    bpy.ops.object.delete()
    scene = bpy.context.scene
    obs = []
    for ob in scene.objects:
        if ob.type == 'MESH':
            obs.append(ob)
    ctx = bpy.context.copy()
    # one of the objects to join
    ctx['active_object'] = obs[0]

    ctx['selected_objects'] = obs

    bpy.ops.object.delete(ctx)
    return directory_replaced + fid + ".obj"

def getObj_object(objfile):
    file_loc=objfile
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    return obj_object


def addObjFile_(dic,outFileName):
    bpy.ops.object.delete()
    for i in range(len(dic)-1):
        file_loc=dic[i].get('fileName')
        location = dic[i].get('xyz')
        angle = dic[i].get('angle')
        print(dic[i].get('fileName'))
        imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
        obj_object = bpy.context.selected_objects[0]
        obj_object.rotation_euler[0] = degreeToEuler(angle[0])
        obj_object.rotation_euler[1] = degreeToEuler(angle[1])
        obj_object.rotation_euler[2] = degreeToEuler(angle[2])
        obj_object.location = [location[0],location[1], location[2]]
    bpy.ops.export_scene.obj(filepath=outFileName)
    bpy.ops.object.delete()
def rotationObjforIfc(savepath,outputfile,objFile,angle):
    '''
    생성된 파일을 json데이터에 있는 좌표와 회전각대로 이동 및 회전시키는 함수
    :param outputfile: 회전 및 이동시킨 파일
    :param objFile: 회전 및 이동시킬 파일
    :param angle: 변경될 회전 각도[pitch,roll,azimuth]
    :return: 생성된 파일 fullpath
    '''
    directory = savepath + '\mapObj\\'
    directory_replaced = directory.replace('\\', '/', 10)
    createFolder(directory_replaced)
    file_loc = objFile
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]
    obj_object.rotation_euler[0] = degreeToEuler(angle[0])
    obj_object.rotation_euler[1] = degreeToEuler(angle[1])
    obj_object.rotation_euler[2] = degreeToEuler(angle[2])
    bpy.ops.export_scene.obj(
        filepath=directory_replaced + outputfile)
    bpy.ops.object.delete()
    return directory_replaced + outputfile


def rotationObj(filePath,Angle):
    '''
     obj file rotation
    :param filePath: obj file path
    :param Angle: angle list[pitch,roll, azimuth]
    :return:
    '''
    file_loc = filePath
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
    scene = bpy.context.scene
    obs = []
    for ob in scene.objects:
        if ob.type == 'MESH':
            obs.append(ob)
    ctx = bpy.context.copy()
    # one of the objects to join
    ctx['active_object'] = obs[0]

    ctx['selected_objects'] = obs
    # In Blender 2.8x this needs to be the following instead:
    # ctx['selected_editable_objects'] = obs

    bpy.ops.object.join(ctx)

    obj_object = bpy.context.selected_objects[0]  ####<--Fix
    obj_object.rotation_euler[0] = degreeToEuler(Angle[0])
    obj_object.rotation_euler[1] = degreeToEuler(Angle[1])
    obj_object.rotation_euler[2] = degreeToEuler(Angle[2])
    bpy.ops.export_scene.obj(filepath=filePath)
    bpy.ops.object.delete()



def exportPipe(pipLst,savepath,jobid,savefile,inputfile,insertimage,inputWidth):
    bpy.ops.object.delete(use_global=False)
    dicFileLocation={}
    for i in range(len(pipLst)):
        width = 0
        height = 0
        type = pipLst[i].get('type')
        geometry = pipLst[i].get('geometry')
        diameter = pipLst[i].get('diameter')
        category = pipLst[i].get('category')
        if category == '3':
            width = pipLst[i].get('width')
            height = pipLst[i].get('height')
        if type == 'line':
            firstlat=geometry[0].get('lat_5186')
            firstlon=geometry[0].get('lon_5186')
            nextlat = geometry[1].get('lat_5186')
            nextlon = geometry[1].get('lon_5186')
            depth = geometry[0].get('depth')
            azimuth = geometry[0].get('azimuth')
            newSize = math.sqrt((firstlon - nextlon) ** 2 + (firstlat - nextlat) ** 2)
            newWidth = diameter
            if newWidth==None: newWidth=inputWidth
            saveFile = savefile + str(0)
            outfile_0 = makePipeResize(savepath, inputfile, insertimage, inputWidth, newSize, newWidth,
                                                  saveFile, jobid)
            dicFileLocation.setdefault("0", [outfile_0, 0, 0, depth,geometry[0]])
            for j in range(len(geometry)):
                lat=geometry[j].get('lat_5186')
                lon=geometry[j].get('lon_5186')
                before_lon=geometry[j-1].get('lon_5186')
                before_lat =geometry[j-1].get('lat_5186')
                depth = geometry[j].get('depth')
                azimuth = geometry[j].get('azimuth')
                newSize = math.sqrt((lon - before_lon) ** 2 + (lat - before_lat) ** 2)
                newWidth = diameter
                if newWidth == None: newWidth = inputWidth
                saveFile = savefile + str(j)

                outfile = makePipeResize(savepath, inputfile, insertimage, inputWidth, newSize, newWidth,
                                                    saveFile, jobid)
                dicFileLocation.setdefault(str(i)+"_"+str(j), [outfile, lon - firstlon, lat - firstlat, depth,geometry[j]])
    return dicFileLocation

def exportObjfromDic(dic,id,savepath,inputfile,insertimage,inputWidth,inputjointfile,insertjointimage,inputHolefile,insertholeimage):
    # 기본 큐브 삭제
    bpy.ops.object.delete(use_global=False)

    for key, value in dic.items():
        if key == 'pipe':
            for i in range(len(value)):
                if str(value[i].get("type")) == "1" or str(value[i].get("type")) == "0":
                    outfile = makePipeResize(savepath, inputfile, insertimage, inputWidth,
                                                        value[i].get("distance") * 100, value[i].get("diameter"),
                                                        "fid" + str(value[i].get("fid")), id)
                    rotationObj(outfile,
                                           [value[i].get("pitch"), value[i].get("roll"), value[i].get("azimuth")])
                elif str(value[i].get("type")) == "4" or str(value[i].get("type")) == "5":
                    print("curve!!!!!!!!!!!!!!!!!!!!!!! :", value[i].get("type"), value[i])
                    frontPipeLocation = []
                    if i == 0:
                        frontPipeLocation = [float(value[i + 1].get('thislon')), float(value[i + 1].get('thislat')),
                                             float(value[i + 1].get('depth'))]
                    else:
                        frontPipeLocation = [float(value[i - 1].get('thislon')), float(value[i - 1].get('thislat')),
                                             float(value[i - 1].get('depth'))]
                        curveLocation = [float(value[i].get('thislon')), float(value[i].get('thislat')),
                                         float(value[i].get('curve_depth'))]
                        degree = float(value[i].get("curve_deg"))
                        outfile = createCurve(savepath, frontPipeLocation, curveLocation, inputfile,
                                                         insertimage, degree,
                                                         value[i].get('fid'), id)
                        rotationObj(outfile,
                                               [value[i].get("pitch"), value[i].get("roll"), value[i].get("azimuth")])
        elif key == 'joint':
            for i in range(len(value)):
                outfile = makeJointResize(savepath, inputjointfile, insertjointimage, 0,
                                                     float(value[i].get("diameter")), "fid" + str(value[i].get("fid")),
                                                     id)
                rotationObj(outfile, [value[i].get("pitch"), value[i].get("roll"), value[i].get("azimuth")])
                # [savepath,iniputfile,insertimage,inputlength,distance(newsize),diameter(newwidth),fid,loginid(jobid),'joint',[pitch,roll,azimuth]???new lengh???
        elif key == 'hole':
            for i in range(len(value)):
                for i in range(len(value)):
                    if value[i].get('obs_type') == 2:
                        outfile = makeHoleCResize(savepath, value[i].get('diameter'),
                                                             value[i].get('hole_depth'), value[i].get('width'),
                                                             value[i].get('cover_diameter'), insertholeimage,
                                                             inputHolefile, "fid" + str(value[i].get('fid')), id)
                        rotationObj(outfile,
                                               [value[i].get("pitch"), value[i].get("roll"), value[i].get("azimuth")])
                        # [savepath,value[i].get("diameter"),value[i].get("diameter"),value[i].get("hole_depth"),value[i].get("corverLength"),value[i].get("cover_diameter"),insertimage,"fid"+value[i].get("fid"),id,C,[pitch,roll,azimuth]]
                    elif value[i].get('obs_type') == 3:
                        outfile = makeHoleSResize(savepath, value[i].get('width'), value[i].get('height'),
                                                             value[i].get('hole_depth'),
                                                             value[i].get('cover_diameter'), insertholeimage,
                                                             inputHolefile, "fid" + str(value[i].get('fid')), id)
                        rotationObj(outfile,
                                               [value[i].get("pitch"), value[i].get("roll"), value[i].get("azimuth")])


############################
# ##########for convert ifc
###########################

def getVertexandMove(location,readFile):
    '''
        Get vertex list from obj file
        :param readFile: obj file full path
        :return: vertex list
        '''
    rf = open(readFile, "r")
    vertexLst = []
    while True:
        line = rf.readline()
        split = line.split()
        if len(split) > 2:
            if split[0] == 'v':
                vtLst = (float(split[1])+location[0], float(split[2])+location[0], float(split[3])+location[0])
                vertexLst.append(vtLst)
        if not line:
            break
    rf.close()
    return vertexLst
def getVertex(readFile):
    '''
    Get vertex list from obj file
    :param readFile: obj file full path
    :return: vertex list
    '''
    rf = open(readFile, "r")
    vertexLst=[]
    while True:
        line = rf.readline()
        split = line.split()
        if len(split) > 2:
            if split[0] == 'v':
                vtLst = (float(split[1]), float(split[2]),float(split[3]))
                vertexLst.append(vtLst)
        if not line:
            break
    rf.close()
    return vertexLst

#get face vertext from objfile
def getface(readFile):
    '''
    Get face list from obj file
    :param readFile: obj file full path
    :return: face list
    '''
    rf = open(readFile, "r")
    faceLst=[]
    while True:
        line = rf.readline()
        split = line.split()
        if len(split) > 2:
            if split[0] == 'f':
                lst=[]
                for f in range(1,len(split)):
                    lst.append(split[f].split('/')[0])
                faceLst.append(lst)
        if not line:
            break
    rf.close()
    return faceLst

def getGroupName(objfileName):
    '''
    Get Group name in obj file for create header
    :param objfileName: obj file full path
    :return: group name (string)
    '''
    if os.path.exists(objfileName):
        rf=open(objfileName,"r")
        while True:
            line=rf.readline()
            split=line.split()
            if len(split)>1:
                if split[0]=="o":
                    rf.close()
                    return split[1]
    else:
        return  "objFile0.1"


def getMtlList(objfileName):
    '''
    Get Mtl file name in obj file for create header
    :param objfileName: obj file name full path
    :return: mtl file name (string)
    '''
    mtlFile = objfileName.split('.obj')[0] + '.mtl'
    mtllst=[]
    dic = {}
    if os.path.exists(mtlFile):
        rf = open(mtlFile, "r")
        while True:
            line = rf.readline()
            split = line.split()
            if len(split) > 1:
                if split[0] == "newmtl":
                    if len(dic)>1:
                        mtllst.append(dic)
                    dic.clear()
                    dic.setdefault("newmtl",split[1])
                elif split[0] == "Kd":
                    if len(split)>2:
                        dic.setdefault("Kd",[float(split[1]),float(split[2]),float(split[3])])
                elif split[0]=="map_Kd":
                    if len(split)>2:
                        dic.setdefault("map_Kd",split[1])
            if not line:
                mtllst.append(dic)
                break
        rf.close()
    return mtllst

def getObjDataforIfc(objfile):
    objList=[]
    #   objfile=fileList[i]
    #   vertextList=obj_editor.getVertex(objfile)
    #   faceList = obj_editor.getface(objfile)
    #   groupName = obj_editor.getGroupName(objfile)
    #   locationList=location[i]
    #   infoList=info[i]

    dic = {}
    vertextList = []
    faceList = []
    infoList = {}
    groupName=""
    if os.path.exists(objfile):
        rf=open(objfile,"r")
        while True:
            line=rf.readline()
            split=line.split()
            if len(split)>1:
                if split[0]=="o":
                    if len(vertextList)>0:
                        dic.setdefault("vertextList",vertextList)
                        dic.setdefault("faceList", faceList)
                        dic.setdefault('groupName',groupName)
                        dic.setdefault('infoList', infoList)
                        objList.append(dic)
                        dic={}
                        faceList=[]
                        vertextList=[]
                    groupName=split[1]
                if split[0]=="v":
                    vtLst = (float(split[1]), float(split[2]), float(split[3]))
                    vertextList.append(vtLst)
                if split[0]=="f":
                    lst = []
                    for f in range(1, len(split)):
                        lst.append(split[f].split('/')[0])
                    faceList.append(lst)
            if not line:
                break
                rf.close()
    return objList


