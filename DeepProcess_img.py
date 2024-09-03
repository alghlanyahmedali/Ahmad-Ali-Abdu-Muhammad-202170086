# import numpy as np
# import math
# def func_formarray(center,theta,selectarr):
#     thta=theta*3.14159265359/180
#     (px,py)=center
#     # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#     arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
#     arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
#     arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
#     arr=np.array((arr2.dot(arr3)).dot(arr4))
    
#     if selectarr>=0:
#         return arr
#     else:
#         arrinvese=np.array(arr.T)
#         arrinvese[3,:3]=0
#         arrtra=np.array(arrinvese.dot(arr[:,3]))
#         arrinvese[:,3]=-arrtra
#         return arrinvese
# # end off func_formarray

# def func_round(pointxy):
#     (x,y)=pointxy
#     xtom=x//1
#     ytom=y//1
#     xch=x-xtom
#     ych=y-ytom
#     xch=xch*1000000
#     ych=ych*1000000
#     if xch>=555555:
#         xtom+=1
#     if ych>=555555:
#         ytom+=1
#     intxy=(int(xtom),int(ytom))
#     return intxy

# def func_rotat(img_arr,center,hwtheta):
#     (h,w,theta)=hwtheta
#     (x02,y02)=center
#     x0=int(h)
#     y0=int(w)
#     T20=np.array(func_formarray(center,theta,1))
#     print(x0,y0)
#     print(T20)
#     arrA=np.array(img_arr)
#     arrB=np.array(img_arr)
#     arrB[:,:]=0
#     print(arrB)
#     # arr[:,:]=0
#     print(arrA.shape)
#     print(arrB.shape)
#     for i in range(0,x0,1): 
#         for j in range(0,y0,1):
#             arr1=np.array([[i],[j],[0],[1]])
#             arrcheck=np.array((T20.dot(arr1)))
#             (chi,chj)=(int(arrcheck[0]),int(arrcheck[1]))
#             if (arrcheck[0]>=0 and arrcheck[0]<h):
#                 if (arrcheck[1]>=0 and arrcheck[1]<w):
#                     if arrB[chi,chj]==0:
#                         arrB[chi,chj]=arrA[i,j]
#                 elif ((chj-1)>=0 and (chj-1)<w):
#                     if arrB[chi,chj-1]==0:
#                         arrB[chi,chj-1]=arrA[i,j]
#                 elif ((chj+1)>=0 and (chj+1)<w):
#                     if arrB[chi,chj+1]==0:
#                         arrB[chi,chj+1]=arrA[i,j]
#             (chi,chj)=(func_round((arrcheck[0],arrcheck[1]))) 
#             if (chi>=0 and chi<h):
#                 if (chj>=0 and chj<w):
#                     if arrB[chi,chj]==0:
#                         arrB[chi,chj]=arrA[i,j]
#                 elif ((chj-1)>=0 and (chj-1)<0):
#                     if arrB[chi,chj-1]==0:
#                         arrB[chi,chj-1]=arrA[i,j]
#                 elif ((chj+1)>=0 and (chj+1)<0):
#                     if arrB[chi,chj+1]==0:
#                         arrB[chi,chj+1]=arrA[i,j]
            
#     return arrB
# import cv2 as cv
# img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (305).png",0)  
# ximg=np.array(img)
# daimimg=img.shape[:2]
# h,w=daimimg
# center=(h/2,w/2)
# # xarr=np.array(func_formarray(center,45,-1))
# imgrot=np.array(func_rotat(ximg,center,(h,w,45)))
# cv.imshow("img",img)
# cv.imshow("imgrot",imgrot)
# cv.waitKey(0)
# cv.destroyAllWindows()













# import numpy as np
# import math
# def func_formarray(center,theta,selectarr):
#     thta=theta*3.14159265359/180
#     (px,py)=center
#     # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#     arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
#     arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
#     arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
#     arr=np.array((arr2.dot(arr3)).dot(arr4))
    
#     if selectarr>=0:
#         return arr
#     else:
#         arrinvese=np.array(arr.T)
#         arrinvese[3,:3]=0
#         arrtra=np.array(arrinvese.dot(arr[:,3]))
#         arrinvese[:,3]=-arrtra
#         return arrinvese
# # end off func_formarray

# def func_round(pointxy):
#     (x,y)=pointxy
#     xtom=x//1
#     ytom=y//1
#     xch=x-xtom
#     ych=y-ytom
#     xch=xch*1000000
#     ych=ych*1000000
#     if xch>=555555:
#         xtom+=1
#     if ych>=555555:
#         ytom+=1
#     intxy=(int(xtom),int(ytom))
#     return intxy

# def func_rotat(img_arr,center,hwtheta):
#     (h,w,theta)=hwtheta
#     (x02,y02)=center
#     x0=int(h)
#     y0=int(w)
#     T20=np.array(func_formarray(center,theta,1))
#     print(x0,y0)
#     print(T20)
#     arrA=np.array(img_arr)
#     arrB=np.array(img_arr)
#     arrB[:,:]=0
#     print(arrB)
#     # arr[:,:]=0
#     print(arrA.shape)
#     print(arrB.shape)
#     for i in range(0,x0,1): 
#         for j in range(0,y0,1):
#             arr1=np.array([[i],[j],[0],[1]])
#             arrcheck=np.array((T20.dot(arr1)))
#             (chi,chj)=(int(arrcheck[0]),int(arrcheck[1]))
#             if (arrcheck[0]>=0 and arrcheck[0]<h):
#                 if ((chj-1)>=0 and (chj-1)<w):
#                     if arrB[chi,chj-1]==0:
#                         arrB[chi,chj-1]=arrA[i,j]
#                 elif (arrcheck[1]>=0 and arrcheck[1]<w):
#                     if arrB[chi,chj]==0:
#                         arrB[chi,chj]=arrA[i,j]
#                 elif ((chj+1)>=0 and (chj+1)<w):
#                     if arrB[chi,chj+1]==0:
#                         arrB[chi,chj+1]=arrA[i,j]
#             (chi,chj)=(func_round((arrcheck[0],arrcheck[1]))) 
#             if (chi>=0 and chi<h):
#                 if (chj>=0 and chj<w):
#                     if arrB[chi,chj]==0:
#                         arrB[chi,chj]=arrA[i,j]
#                 elif ((chj-1)>=0 and (chj-1)<w):
#                     if arrB[chi,chj-1]==0:
#                         arrB[chi,chj-1]=arrA[i,j]
#                 elif ((chj+1)>=0 and (chj+1)<w):
#                     if arrB[chi,chj+1]==0:
#                         arrB[chi,chj+1]=arrA[i,j]
            
#     return arrB
# import cv2 as cv
# img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (305).png",0)  
# ximg=np.array(img)
# daimimg=img.shape[:2]
# h,w=daimimg
# center=(h/2,w/2)
# # xarr=np.array(func_formarray(center,45,-1))
# imgrot=np.array(func_rotat(ximg,center,(h,w,45)))
# cv.imshow("img",img)
# cv.imshow("imgrot",imgrot)
# cv.waitKey(0)
# cv.destroyAllWindows()











# import numpy as np
# import math
# def func_formarray(center,theta,selectarr):
#     thta=theta*3.14159265359/180
#     (px,py)=center
#     # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#     arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
#     arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
#     arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
#     arr=np.array((arr2.dot(arr3)).dot(arr4))
    
#     if selectarr>=0:
#         return arr
#     else:
#         arrinvese=np.array(arr.T)
#         arrinvese[3,:3]=0
#         arrtra=np.array(arrinvese.dot(arr[:,3]))
#         arrinvese[:,3]=-arrtra
#         return arrinvese
# # end off func_formarray

# def func_round(pointxy):
#     (x,y)=pointxy
#     xtom=x//1
#     ytom=y//1
#     xch=x-xtom
#     ych=y-ytom
#     xch=xch*1000000
#     ych=ych*1000000
#     if xch>=555555:
#         xtom+=1
#     if ych>=555555:
#         ytom+=1
#     intxy=(int(xtom),int(ytom))
#     return intxy

# def func_rotat(img_arr,center,hwtheta):
#     (h,w,theta)=hwtheta
#     (x02,y02)=center
#     x0=int(h)
#     y0=int(2*w)
#     T20=np.array(func_formarray(center,theta,1))
#     T21=np.array([[T20[0,0],T20[0,1],T20[0,3]],[T20[1,0],T20[1,1],T20[1,3]]])
#     print(x0,y0)
#     print(T21)
#     arrA=np.array(img_arr)
#     arrB=np.array(img_arr)
#     arrB[:,:]=0
#     # arr[:,:]=0
#     print(arrA.shape)
#     print(arrB.shape)
#     for i in range(0,x0,1):
#         # cv.imshow("imgrot",arrB) 
#         for j in range(0,y0,1):
#             arr1=np.array([[i],[j/2],[1]])
#             arrcheck=np.array((T21.dot(arr1)))
#             (chi,chj)=(func_round((arrcheck[0],arrcheck[1])))
#             if (chi>=0 and chi<h and chj>=0 and chj<w):
#                 (xi,xj)=(func_round((i,j/2))) 
#                 arrB[chi,chj-1]=arrA[xi,xj]
#         # cv.waitKey(0)
#         # cv.destroyAllWindows() 
#     return arrB
# import cv2 as cv
# img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (36).png",0)  
# ximg=np.array(img)
# daimimg=img.shape[:2]
# (h,w)=daimimg
# center=(h/2,w/2)
# print(center,h,w)
# # xarr=np.array(func_formarray(center,45,-1))
# imgrot=np.array(func_rotat(ximg,center,(h,w,-45)))
# cv.imshow("img",img)
# cv.imshow("imgrot",imgrot)
# cv.waitKey(0)
# cv.destroyAllWindows()





# import numpy as np
# import math
# def func_formarray(center,theta,selectarr):
#     thta=theta*3.14159265359/180
#     (px,py)=center
#     # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#     arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
#     arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
#     arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
#     arr=np.array((arr2.dot(arr3)).dot(arr4))
    
#     if selectarr>=0:
#         return arr
#     else:
#         arrinvese=np.array(arr.T)
#         arrinvese[3,:3]=0
#         arrtra=np.array(arrinvese.dot(arr[:,3]))
#         arrinvese[:,3]=-arrtra
#         return arrinvese
# # end off func_formarray

# def func_round(pointxy):
#     (x,y)=pointxy
#     xtom=x//1
#     ytom=y//1
#     xch=x-xtom
#     ych=y-ytom
#     xch=xch*1000000
#     ych=ych*1000000
#     if xch>=555555:
#         xtom+=1
#     if ych>=555555:
#         ytom+=1
#     intxy=(int(xtom),int(ytom))
#     return intxy

# def func_rotat(img_arr,center,hwtheta):
#     (h,w,theta)=hwtheta
#     (x02,y02)=center
#     x0=int(h)
#     y0=int(w)
#     T02=np.array(func_formarray(center,theta,-1))
#     T12=np.array([[T02[0,0],T02[0,1],T02[0,3]],[T02[1,0],T02[1,1],T02[1,3]]])
#     print(x0,y0)
#     print(T21)
#     arrA=np.array(img_arr)
#     arrB=np.array(img_arr)
#     arrB[:,:]=0
#     # arr[:,:]=0
#     print(arrA.shape)
#     print(arrB.shape)
#     for i in range(0,x0,1):
#         # cv.imshow("imgrot",arrB) 
#         for j in range(0,y0,1):
#             arr1=np.array([[i],[j],[1]])
#             arrcheck=np.array((T12.dot(arr1)))
#             (chi,chj)=(func_round((arrcheck[0],arrcheck[1])))
#             if (chi>=0 and chi<h and chj>=0 and chj<w):
#                 (xi,xj)=(func_round((i,j/2))) 
#                 arrB[chi,chj]=arrA[xi,xj]
#         # cv.waitKey(0)
#         # cv.destroyAllWindows() 
#     return arrB
# import cv2 as cv
# img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (36).png",0)  
# ximg=np.array(img)
# daimimg=img.shape[:2]
# (h,w)=daimimg
# center=(h/2,w/2)
# print(center,h,w)
# # xarr=np.array(func_formarray(center,45,-1))
# imgrot=np.array(func_rotat(ximg,center,(h,w,-45)))
# cv.imshow("img",img)
# cv.imshow("imgrot",imgrot)
# cv.waitKey(0)
# cv.destroyAllWindows()






# import numpy as np
# import math
# def func_formarray(center,theta,selectarr):
#     thta=theta*3.14159265359/180
#     (px,py)=center
#     # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#     arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
#     arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
#     arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
#     arr=np.array((arr2.dot(arr3)).dot(arr4))
    
#     if selectarr>=0:
#         return arr
#     else:
#         arrinvese=np.array(arr.T)
#         arrinvese[3,:3]=0
#         arrtra=np.array(arrinvese.dot(arr[:,3]))
#         arrinvese[:,3]=-arrtra
#         return arrinvese
# # end off func_formarray

# def func_round(pointxy):
#     (x,y)=pointxy
#     xtom=x//1
#     ytom=y//1
#     xch=x-xtom
#     ych=y-ytom
#     xch=xch*10
#     ych=ych*10
#     if xch>=5:
#         xtom+=1
#     if ych>=5:
#         ytom+=1
#     intxy=(int(xtom),int(ytom))
#     return intxy

# def func_rotat(img_arr,center,hwtheta):
#     (h,w,theta)=hwtheta
#     (x02,y02)=center
#     x0=int(h)
#     y0=int(w)
#     T20=np.array(func_formarray(center,theta,-1))
#     T21=np.array([[T20[0,0],T20[0,1],T20[0,3]],[T20[1,0],T20[1,1],T20[1,3]]])
#     print(x0,y0)
#     print(T21)
#     arrA=np.array(img_arr)
#     arrB=np.array(img_arr)
#     arrB[:,:]=0
#     arr1=np.array([[0],[0],[1]])
#     print(arrA.shape)
#     print(arrB.shape) 
#     for i in range(0,x0,1):
#         for j in range(0,y0,1):
#             arr1=[[i],[j],[1]]
#             arrcheck=np.array((T21.dot(arr1)))
#             (chi,chj)=(func_round((arrcheck[0],arrcheck[1])))
#             if (chi>=0 and chi<h and chj>=0 and chj<w):
#                 arrB[i,j]=arrA[chi,chj] 
#             else:                            
#                 (chi,chj)=(int(arrcheck[0]),int(arrcheck[1]))
#                 if (chi>=0 and chi<h and chj>=0 and chj<w):
#                     arrB[i,j]=arrA[chi,chj]
#         # cv.imshow("imgrot",arrB)
#         # cv.waitKey(0)
#         # cv.destroyAllWindows()
#     return arrB
# import cv2 as cv
# img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (36).png",0)  
# ximg=np.array(img)
# daimimg=img.shape[:2]
# (h,w)=daimimg
# center=(h/2,w/2)
# print(center,h,w)
# # xarr=np.array(func_formarray(center,45,-1))
# imgrot=np.array(func_rotat(ximg,center,(h,w,45)))
# cv.imshow("img",img)
# cv.imshow("imgrot",imgrot)
# cv.waitKey(0)
# cv.destroyAllWindows()




# import numpy as np
# import math
# def func_formarray(center,theta,selectarr):
#     thta=theta*3.14159265359/180
#     (px,py)=center
#     # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#     arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
#     arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
#     arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
#     arr=np.array((arr2.dot(arr3)).dot(arr4))
    
#     if selectarr>=0:
#         return arr
#     else:
#         arrinvese=np.array(arr.T)
#         arrinvese[3,:3]=0
#         arrtra=np.array(arrinvese.dot(arr[:,3]))
#         arrinvese[:,3]=-arrtra
#         return arrinvese
# # end off func_formarray

# def func_round(pointxy):
#     (x,y)=pointxy
#     xtom=x//1
#     ytom=y//1
#     xch=x-xtom
#     ych=y-ytom
#     xch=xch*1000000
#     ych=ych*1000000
#     if xch>=555555:
#         xtom+=1
#     if ych>=555555:
#         ytom+=1
#     intxy=(int(xtom),int(ytom))
#     return intxy

# def func_rotat(img_arr,center,hwtheta):
#     (h,w,theta)=hwtheta
#     (x02,y02)=center
#     x0=int(h)
#     y0=int(w)
#     T20=np.array(func_formarray(center,theta,1))
#     T21=np.array([[T20[0,0],T20[0,1],T20[0,3]],[T20[1,0],T20[1,1],T20[1,3]]])
#     print(x0,y0)
#     print(T21)
#     arrA=np.array(img_arr)
#     arrB=np.array(img_arr)
#     arrC=np.array(img_arr)
#     arrB[:,:]=0
#     arrC[:,:]=0
#     arr1=np.array([[0],[0],[1]])
#     print(arrA.shape)
#     print(arrB.shape) 
#     for i in range(0,x0,1):
#         for j in range(0,y0,1):
#             arr1=[[i],[j],[1]]
#             arrcheck=np.array((T21.dot(arr1)))
#             (chi,chj)=(func_round((arrcheck[0],arrcheck[1])))
#             if (chi>=0 and chi<h and chj>=0 and chj<w and arrC[chi,chj]==0):
#                 arrB[i,j]=arrA[chi,chj]
#                 arrC[chi,chj]=1
#                 # print(i,j,chi,chj,arrC[chi,chj])
#             else:
#                 (chi,chj)=(int(arrcheck[0]),int(arrcheck[1]))
#                 if (chi>=0 and chi<h and chj>=0 and chj<w and arrC[chi,chj]==0):
#                     arrB[i,j]=arrA[chi,chj] 
#                     arrC[chi,chj]=2
#                     # print(i,j,chi,chj,arrC[chi,chj])                         
#         # cv.imshow("imgrot",arrB)
#         # cv.waitKey(0)
#         # cv.destroyAllWindows()
#     return arrB
# import cv2 as cv
# img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (36).png",0)  
# ximg=np.array(img)
# daimimg=img.shape[:2]
# (h,w)=daimimg
# center=(h/2,w/2)
# print(center,h,w)
# # xarr=np.array(func_formarray(center,45,-1))
# imgrot=np.array(func_rotat(ximg,center,(h,w,45)))
# cv.imshow("img",img)
# cv.imshow("imgrot",imgrot)
# cv.waitKey(0)
# cv.destroyAllWindows()





import numpy as np
import math
import cv2 as cv
def func_formarray(center,theta,selectarr):
    thta=theta*3.14159265359/180
    (px,py)=center
    # arr1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
    arr2=np.array([[1,0,0,px],[0,1,0,py],[0,0,1,0],[0,0,0,1]])
    arr3=np.array([[math.cos(thta),-math.sin(thta),0,0],[math.sin(thta),math.cos(thta),0,0],[0,0,1,0],[0,0,0,1]])
    arr4=np.array([[1,0,0,-px],[0,1,0,-py],[0,0,1,0],[0,0,0,1]])
    arr=np.array((arr2.dot(arr3)).dot(arr4))
    
    if selectarr>=0:
        return arr
    else:
        arrinvese=np.array(arr.T)
        arrinvese[3,:3]=0
        arrtra=np.array(arrinvese.dot(arr[:,3]))
        arrinvese[:,3]=-arrtra
        return arrinvese
# end off func_formarray

def func_round(pointxy):
    (x,y)=pointxy
    xtom=x//1
    ytom=y//1
    xch=x-xtom
    ych=y-ytom
    xch=xch*1000000
    ych=ych*1000000
    if xch>=555555:
        xtom+=1
    if ych>=555555:
        ytom+=1
    intxy=(int(xtom),int(ytom))
    return intxy

def func_rotat(img_arr,center,hwtheta):
    (h,w,theta)=hwtheta
    (x02,y02)=center
    x0=int(5*h)
    y0=int(5*w)
    T20=np.array(func_formarray(center,theta,1))
    T21=np.array([[T20[0,0],T20[0,1],T20[0,3]],[T20[1,0],T20[1,1],T20[1,3]]])
    print(x0,y0)
    print(T21)
    arrA=np.array(img_arr)
    arrB=np.array(img_arr)
    arrC=np.array(img_arr)
    arrD=np.array(img_arr)
    arrB[:,:]=0
    arrC[:,:]=0
    arrD[:,:]=0
    arr1=np.array([[0],[0],[1]])
    print(arrA.shape)
    print(arrB.shape) 
    for i in range(0,x0,1):
        for j in range(0,y0,1):
            arr1=[[i/5],[j/5],[1]]
            arrcheck=np.array((T21.dot(arr1)))
            (chi,chj)=(int(arrcheck[0]),int(arrcheck[1]))
            (xi,xj)=(int(i/5),int(j/5))
            if (chi>=0 and chi<h and chj>=0 and chj<w and arrC[chi,chj]==0):
                if (xi>=0 and xi<h and xj>=0 and xj<w and arrD[xi,xj]==0):
                    arrB[xi,xj]=arrA[chi,chj]
                    arrC[chi,chj]=1
                    arrD[xi,xj]=1
                    # print(i,j,chi,chj,arrC[chi,chj])
            else:
                (chi,chj)=(func_round((arrcheck[0],arrcheck[1])))
                (xi,xj)=(func_round((i/5,j/5)))
                if (chi>=0 and chi<h and chj>=0 and chj<w and arrC[chi,chj]==0):
                    if (xi>=0 and xi<h and xj>=0 and xj<w and arrD[xi,xj]==0):
                        arrB[xi,xj]=arrA[chi,chj] 
                        arrC[chi,chj]=2
                        arrD[xi,xj]=2
                    # print(i,j,chi,chj,arrC[chi,chj])                         
        # cv.imshow("imgrot",arrB)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
    return arrB

img=cv.imread("C:\\Users\\lenovo\\Desktop\MSD\\opencv_python\\Screenshot (36).png",0)  
ximg=np.array(img)
daimimg=img.shape[:2]
(h,w)=daimimg
center=(h/2,w/2)
print(center,h,w)
# xarr=np.array(func_formarray(center,45,-1))
imgrot=np.array(func_rotat(ximg,center,(h,w,45)))
cv.imshow("img",img)
cv.imshow("imgrot",imgrot)
print(imgrot)
cv.waitKey(0)
cv.destroyAllWindows()