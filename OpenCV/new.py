import random
import cv2
import argparse
import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('folder created')

def extract_frames_from_video(input_path, output_path):
    create_directory(output_path)
    
    video = cv2.VideoCapture(0)
    currentframe = 0

    while True:
        ret, frame = video.read()
        
        # cv2.imshow('frame', frame)
        # save image 
        img_type = '.jpg'
        # smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        
        cv2.imshow('frame', frame)
        #create directory
        # file_path = create_directory(path)
        full_path = f'{output_path + str(currentframe) + img_type}'
        print('creating ............', full_path)
        
        # save current frame
        cv2.imwrite(full_path, frame)
        
        currentframe += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
        
        
        
    video.release()

    video.destroyAllWindows()
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', dest='folder', type=str, required=True, help='directory to save resulting frames')
    parser.add_argument('--video', dest='input_path', type=str, required=True, help='the name of the video')
    # parser.add_argument('filename', dest='filename', type=str, required=True)
    
    args = parser.parse_args()
    print(args)
    
    # create_directory(args.folder)
    extract_frames_from_video(args.input_path, args.output_path)
    main()