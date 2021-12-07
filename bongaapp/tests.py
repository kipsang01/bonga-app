from django.test import TestCase
from .models import  Image,Comment, Like
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user1 = User(username='psang',first_name='Enock',last_name ='kipsang',email='psang254@gmail.com',password ='sjsiuwueufbccn')
        self.image1 = Image(image='peak.jpg',name='peak',caption='mountain peak',author=self.user1,location='nairobi')
        self.comment1 = Comment(author=self.user1,image=self.image1,content='Awesome')
        self.like1= Like(author =self.user1,image=self.image1)
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.image1,Image))
        self.assertTrue(isinstance(self.comment1,Comment))
        self.assertTrue(isinstance(self.like1,Like))
        
    # Testing Save Method
    def test_save_method(self):
        self.user1.save()
        self.image1.save_image()
        self.comment1.save_comment()
        self.like1.save_like()
        users = User.objects.all()
        images = Image.objects.all()
        comments = Comment.objects.all()
        likes = Like.objects.all()
        self.assertTrue(len(images) > 0)
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(comments) > 0)
        self.assertTrue(len(likes) > 0)
     
    #   # Testing Delete Method   
    # def test_delete(self):
    #     self.location1.save_location()
    #     self.category1.save_category()
    #     self.image1.save_image()
    #     Image.objects.get(id =self.image1.id).delete()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images) == 0)
       
    #    # Testing Get Image by Id 
    # def test_get_image_by_id(self):
    #     self.location1.save_location()
    #     self.category1.save_category()
    #     self.image1.save_image()
    #     image = Image.get_image_by_id(self.image1.id)
    #     self.assertTrue(image is not None)
        
    #     # Testing Update image
        
    # def test_update_image(self):
    #     self.location1.save_location()
    #     self.category1.save_category()
    #     self.image1.save_image()
    #     image = Image.get_image_by_id(self.image1.id)
    #     image.update_image('peak.jpg')
    #     image = Image.get_image_by_id(self.image1.id)
    #     self.assertTrue(image.image == 'peak.jpg')