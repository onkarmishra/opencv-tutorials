import cv2
import numpy as np 
import os
import argparse


def seamless_clone(input_src_image_path:str, input_dst_image_path: str, output_dir: str):
    
    os.makedirs(args.output_dir,exist_ok=True)
    output_file_normal = os.path.join(args.output_dir,"seamless_normal_clone.jpg")
    output_file_mixed = os.path.join(args.output_dir,"seamless_mixed_clone.jpg")

    # Read images
    src = cv2.imread(input_src_image_path)
    dst = cv2.imread(input_dst_image_path)

    # Create a rough mask around the airplane.
    src_mask = np.zeros(src.shape, src.dtype)
    #poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
    poly = np.array([ [0,40], [300,40], [300,140], [0,140] ], np.int32)
    cv2.fillPoly(src_mask, [poly], (255, 255, 255))

    # This is where the CENTER of the airplane will be placed
    center = (800,100)

    # Clone seamlessly.
    output_normal = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
    #output_mixed = cv2.seamlessClone(src, dst, src_mask, center, cv2.MIXED_CLONE)


    # Write result
    #cv2.imwrite("images/opencv-seamless-cloning.jpg", output)
    cv2.imwrite(output_file_normal, output_normal)
    #cv2.imwrite(output_file_mixed, output_mixed)

##################  Help ######################
'''
python seamless_cloning.py --input_src_image_path ./images/airplane.jpg --input_dst_image_path ./images/sky.jpg --output_dir ./images/output
'''
###############################################    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seamless clone source image into destinantion image using opencv")
    parser.add_argument("--input_src_image_path",required=True,type=str,help="input source image path1")
    parser.add_argument("--input_dst_image_path",required=True,type=str,help="input destination image path")
    parser.add_argument("--output_dir",required=True,type=str,help="input source image path")
    
    args = parser.parse_args()

 
    seamless_clone(args.input_src_image_path,args.input_dst_image_path, args.output_dir)
   

