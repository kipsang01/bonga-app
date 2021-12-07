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
     
      # Testing Delete Method   
    def test_delete(self):
        self.user1.save()
        self.image1.save_image()
        self.comment1.save_comment()
        self.like1.save_like()
        Like.objects.get(id =self.like1.id).delete()
        Comment.objects.get(id =self.comment1.id).delete()
        Image.objects.get(id =self.image1.id).delete()
        User.objects.get(id =self.user1.id).delete()
        images = Image.objects.all()
        comments = Comment.objects.all()
        likes = Like.objects.all()
        users = User.objects.all()
        self.assertTrue(len(images) == 0)
        self.assertTrue(len(comments) == 0)
        self.assertTrue(len(likes) == 0)
        self.assertTrue(len(users) == 0)
    
    
      # Testing update method   
    def test_update(self):
        self.user1.save()
        self.image1.save_image()
        self.image1.update_caption('Good')
        updated_caption =self.image1.caption
        self.assertEqual(updated_caption, 'Good')
        
        
      # Test get all images 
    def test_get_all_images(self):
        self.image2 = Image(image='mountain.jpg',name='mountain peak',caption='Glaciers in the peak',author=self.user1,location='mt.kenya')
         
        self.user1.save()
        self.image1.save_image()
        self.image2.save_image()
        images = Image.all_images()
        self.assertTrue(len(images) == 2)
        
        
        
        
        
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