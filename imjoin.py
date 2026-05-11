from PIL import Image
import numpy as np
import sys

sideref=['along width','along height']
other_axis=[1,0]
def usage():
  print('Usage - python imjoin.py image1 image2 side out_image')
  print('image1 - path to first image')
  print('image2 - path to second image')
  print('side -')
  for i in range(len(sideref)):
    print('{:5d} - {:s}'.format(i,sideref[i]))
  print('out_image - output image path')

if len(sys.argv)==5:
  if int(sys.argv[3])==0 or int(sys.argv[3])==1:
    im1=sys.argv[1]
    im2=sys.argv[2]
    side=int(sys.argv[3])
    imo=sys.argv[4]
    print('{:<15s}{:s}'.format('Image 1',im1))
    print('{:<15s}{:s}'.format('Image 2',im2))
    print('{:<15s}{:s}'.format('Joined',sideref[side]))
    print('{:<15s}{:s}'.format('Out Image',imo))
    arra=np.array(Image.open(im1))
    arrb=np.array(Image.open(im2))
    print(arra.shape)
    print(arrb.shape)
    if arra.shape[side]>arrb.shape[side]:
      if side==0:
        arrb=np.array(Image.open(im2).resize((int(arra.shape[side]*arrb.shape[1]/arrb.shape[side]),arra.shape[side]),Image.Resampling.LANCZOS))
      if side==1:
        arrb=np.array(Image.open(im2).resize((arra.shape[side],int(arra.shape[side]*arrb.shape[0]/arrb.shape[side])),Image.Resampling.LANCZOS))
    if arra.shape[side]<arrb.shape[side]:
      if side==0:
        arra=np.array(Image.open(im2).resize((int(arrb.shape[side]*arra.shape[1]/arra.shape[side]),arrb.shape[side]),Image.Resampling.LANCZOS))
      if side==1:
        arra=np.array(Image.open(im2).resize((arrb.shape[side],int(arrb.shape[side]*arra.shape[0]/arra.shape[side])),Image.Resampling.LANCZOS))
    print(arra.shape)
    print(arrb.shape)
    Image.fromarray(np.concatenate((arra,arrb),axis=other_axis[side])).save(imo)
  else:
    usage()
else:
  usage()

