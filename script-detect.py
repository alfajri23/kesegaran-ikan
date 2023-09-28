import torch
# model = torch.hub.load('.', 'custom', path='custom-model/eye-detect-dual.pt', source='local') 
# # Image
# img = 'images/makarel-bad-1.jpg'
# # Inference
# results = model(img)
# # Results, change the flowing to: results.show()
# results.crop()  # or .show(), .save(), .crop(), .pandas(), etc

# model2 = torch.hub.load('.', 'custom', path='custom-model/classify-segar-tdk.pt', source='local') 
# # Image
# # img2 = 'runs/detect/exp12/crops/eye/makarel-bad-1.jpg'
# # img2 = 'runs/detect/exp16/makarel-bad-1-eye.jpg'
# img2 = 'images/eye-bad-1.jpg'
# # Inference
# results2 = model2(img2)
# # Results, change the flowing to: results.show()
# results2.show()  # or .show(), .save(), .crop(), .pandas(), etc

def load_image_st(self):
        uploaded_img=st.file_uploader(label='Upload an image')
        if type(uploaded_img) != type(None):
            self.img_data=uploaded_img.getvalue()
            st.image(self.img_data)
            self.im0=Image.open(BytesIO(self.img_data))
            self.im0=np.array(self.im0)

            return self.im0
        elif type(self.im0) !=type(None):
            return self.im0
        else:
            return None