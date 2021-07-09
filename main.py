# This is a sample Python script.
import data_generator
import decimal
import obj_editor
import ifc_creator
import json
import sys
import platform
import argparse
import math
import os

# external module import
if ('Win' in platform.system()):
    externalModule = 'C:\Program Files\Blender Foundation\Blender 2.81\2.81\scripts\modules'
else:
    externalModule = 'G:\Data\python\ObjCreater_fromJson'

sys.path.insert(0, externalModule)
if '--' in sys.argv:
    argv = sys.argv[sys.argv.index('--') + 1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('-s1', '--id', dest='id', type=str, required=True)  #  loginidh
    parser.add_argument('-s2', '--password', dest='password', type=str, required=True)  # login password
    parser.add_argument('-s3', '--url', dest='url', type=str, required=True)#url
    parser.add_argument('-s4', '--savepath', dest='savepath', type=str, required=True)  # obj file save path
    parser.add_argument('-s5', '--inputfile', dest='inputfile', type=str, required=True)  # pipe file full path
    parser.add_argument('-s6', '--insertimage', dest='insertimage', type=str, required=False)  # pipe file texture image full path
    parser.add_argument('-s7', '--inputWidth', dest='inputWidth', type=int,required=True)  # pipe file diameter
    parser.add_argument('-s8', '--inputjointfile', dest='inputjointfile', type=int, required=True)  # joint file full path
    parser.add_argument('-s9', '--insertjointimage', dest='insertjointimage', type=str, required=False)  # joint texture image file full path
    parser.add_argument('-s10', '--inputHolefile', dest='inputHolefile', type=str, required=True)  #  hole cover file full path
    parser.add_argument('-s11', '--insertholeimage', dest='insertholeimage', type=str, required=False)  #  hole cover texture image file full path

    args = parser.parse_known_args(argv)[0]

    savepath = args.savepath
    inputfile = args.inputfile
    insertimage = args.insertimage
    inputWidth = args.inputWidth
    inputjointfile = args.inputjointfile
    insertjointimage = args.insertjointimage
    inputHolefile = args.inputHolefile
    insertholeimage = args.insertholeimage
    password=args.password
    url=args.url
    json=data_generator.getJsonData(id,password,url)
    dic = data_generator.getFromJsonToDic(json)
    obj_editor.exportObjfromDic(dic,id,savepath,inputfile,insertimage,inputWidth,inputjointfile,insertjointimage,inputHolefile,insertholeimage)

else:
  id = "gnsea12"
  password = "move123456"
  url = "https://digitaltwinx.kr/data/"
  savepath = "I:\Data\python\Objwriter"
  inputfile = "I:\Data\python\Obj\pipe\pipe-8.0m.obj"
  insertimage = "I:\Data\python\Obj\pipe\Low_pipe_8_0m_BaseColor.png"
  inputjointfile = "I:\Data\python\Obj\joint\joint-700mm_normal.obj"
  insertjointimage = "I:\Data\python\Obj\joint\map_bump Map__7_Normal_Bump.png"
  insertholeimage = "I:\Data\python\Objwriter\hole\766mm\Map__1_Normal_Bump.png"
  inputHolefile = os.path.join("I:", "Data", "python", "Objwriter", "hole", "766mm", "766m_hole.obj")
  inputWidth = 600
  inputjointwidth = 700
  jsonPath = "I:\Data\python\ObjCreator_fromJson\V1.4_20210616.JSON"
  json = data_generator._loadJsonFile(jsonPath)
  start=695 #시작 group no
  end=700 #종료 group no
  groupNoList=[638]
  filename="20210705_"
  # dic=data_generator.getDicforCreateObjFromJson_groupNoList(json,groupNoList)
  dic = data_generator.getDicforCreateObjFromJson_range(json, start,end)
  straight=dic.get('pipe').get('straight')
  centerIdxi = int(len(straight) / 2)
  if centerIdxi>0:
      centerIdxj = int(len(straight[centerIdxi]) / 2)
  else :
      centerIdxj=0
  pipeList=[]
  for i in range(len(straight)):
    center = [straight[centerIdxi][centerIdxj].get('location')[0],
            straight[centerIdxi][centerIdxj].get('location')[1], straight[centerIdxi][centerIdxj].get('location')[2]]
    for j in range(len(straight[i])):
      azimuth =straight[i][j].get('theta')# (straight[i][j].get('azimuth_2') - straight[i][j].get('azimuth')) +straight[i][j].get('azimuth')
      angle = [straight[i][j].get('pitch'), straight[i][j].get('roll'), straight[i][j].get('theta')]
      angle_ifc=[angle[0],angle[1]-19,angle[2]+19]
      xyz=[straight[i][j].get('location')[0]-center[0],(straight[i][j].get('location')[1]-center[1])*-1,straight[i][j].get('location')[2]*-1]
      straight[i][j].setdefault('xyz',xyz)
      straight[i][j].setdefault('angle', angle)
      diameter=straight[i][j].get('diameter')
      if diameter==None:
          diameter=straight[i][j].get('width')
      pipe=obj_editor.makePipeResize(savepath,inputfile,insertimage,inputWidth,straight[i][j].get('length'),diameter,id)
      straight[i][j].setdefault('fileName',pipe)
      mapfile=obj_editor.rotationObjforIfc(savepath,"pipe-"+str(straight[i][j].get('length'))+"_"+str(straight[i][j].get('azimuth'))+".obj",pipe,angle_ifc)
      straight[i][j].setdefault('mapfile',mapfile)
      pipeList.append(straight[i][j])
  # obj_editor.addObjFile_(pipeList, os.path.join(savepath, filename + "638.obj"))
  # obj_editor.rotationObj(os.path.join(savepath, filename + "687688689.obj"),[-90,0,90])
  obj_editor.addObjFile_(pipeList,os.path.join(savepath,filename+str(start)+"_"+str(end)+".obj"))
  for i in range(len(pipeList)):
      print("groupNo :",pipeList[i].get('groupNo'),"diameter :",pipeList[i].get('diameter'),"xyz :",pipeList[i].get('xyz'),"angle :",pipeList[i].get('angle'),pipeList[i].get('azimuth'))
  #
  #
  # newFile="20210702_.ifc"
  # # # #
  # ifcfile = ifc_creator.getTempIfcfile(newFile)
  # vertextList = obj_editor.getVertex(os.path.join(savepath, filename + "687688689.obj"))
  # faceList = obj_editor.getface(os.path.join(savepath, filename + "687688689.obj"))
  # groupName = obj_editor.getGroupName(os.path.join(savepath, filename + "687688689.obj"))
  # mtlList = obj_editor.getMtlList(os.path.join(savepath, filename + "687688689.obj"))
  # locationList = [0,0,0]
  # infoList = pipeList[0]
  # ifcfile = ifc_creator.addObjecttoIfcFile(ifcfile, newFile, infoList, vertextList, faceList, mtlList, locationList,
  #                                          groupName)
  # ifcfile.write(os.path.join(savepath, newFile))
  # for i in range(len(pipeList)):
  #     vertextList=obj_editor.getVertex(pipeList[i].get("mapfile"))
  #     faceList = obj_editor.getface(pipeList[i].get("mapfile"))
  #     groupName = obj_editor.getGroupName(pipeList[i].get("mapfile"))
  #     mtlList=obj_editor.getMtlList(pipeList[i].get("mapfile"))
  #     locationList =pipeList[i].get('xyz')
  #     infoList = pipeList[i]
  #     ifcfile = ifc_creator.addObjecttoIfcFile(ifcfile, newFile, infoList, vertextList, faceList, mtlList,locationList, groupName)
  # ifcfile.write(os.path.join(savepath, newFile))











