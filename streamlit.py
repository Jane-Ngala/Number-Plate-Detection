#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().system('pip install streamlit')
get_ipython().system('pip install tensorflow')
get_ipython().system('pip install opencv-python')


# In[13]:


import streamlit as st
import cv2
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image,ImageEnhance
import os


# In[22]:


def main():
    """Number Plate Detection App"""
    
    st.title('Number Plate Detection App')
    st.text('Built with Streamlit and OpenCV')
    
    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    if choice =='Detection':
        st.subheader("Number Plate Detection")
        
    elif choice == 'About':
            st.subheader("About")
            
            
            image_file = st.file_uploader("Upload Image", type =['jpg','png','jpeg'])
        
            if image_file is not None:
                our_image = Image.open(image_file)
                st.text("Original Image")
                
# st.write(type(our_image))

                st.image(our_image)

            enhance_type = st.sidebar.radio("Enhance Type",["Original","Gray-Scale","Contrast","Brightness","Blurring"])
            if enhance_type == 'Gray-Scale':
                new_img = np.array(our_image.convert('RGB'))
                img = cv2.cvtColor(new_img,1)
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                
# st.write(new_img)

                st.image(gray)
            elif enhance_type == 'Contrast':
                c_rate = st.sidebar.slider("Contrast",0.5,3.5)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            elif enhance_type == 'Brightness':
                c_rate = st.sidebar.slider("Brightness",0.5,3.5)
                enhancer = ImageEnhance.Brightness(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            elif enhance_type == 'Blurring':
                new_img = np.array(our_image.convert('RGB'))
                blur_rate = st.sidebar.slider("Brightness",0.5,3.5)
                img = cv2.cvtColor(new_img,1)
                blur_img = cv2.GaussianBlur(img,(11,11),blur_rate)
                st.image(blur_img)

            elif enhance_type == 'Original':
                st.image(our_image,width=300)
            else:
                st.image(our_image,width=300)



             

if __name__ == '__main__':
            main()	
    
    


# In[ ]:




