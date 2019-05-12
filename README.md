# social-group

## Live Site
[Live on Heroku](https://social-group-django.herokuapp.com): https://social-group-django.herokuapp.com
![profile]
![post_preview]
![lg_screen]

## Run Locally  
<details>
  <summary>Detail (click to expand)</summary>

**Clone project**
```
git clone https://github.com/jasonx1011/social-group.git  
```
**If you are using Anaconda, do the following commands before virtualenv commands**
```
conda create -n py362 python=3.6.2
source activate py362
condo install virtualenv
```
**Using virtualenv venv**

```
virtualenv venv
source venv/bin/activate

pip install django==1.11
pip install -r requirements.txt
```
**Run Django**
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
</details>

## Features

Social Group is a responsive web application using `Django` MTV (Model-Template-View) framework with Class-Based Views (CBV). Front end is powered by HTML5, CSS3, JavaScript, Masonry, and Bootstrap 3. This application contains the following features with clean and smooth user experience.

### Sample Class-Based Views Code Snippets
```python
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('image_url', 'name', 'description')
    model = Group


class UpdateGroup(LoginRequiredMixin, generic.UpdateView):
    fields = ('image_url', 'name', 'description')
    model = Group
    template_name_suffix = '_update_form'

    def get_object(self, *args, **kwargs):
        group = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return group


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group
```

### Responsive Design 
   * **Large screen: 4 columns**
![lg_screen]
   * **Middle screen: 2 columns without shrinking the image**
![md_screen]
   * **Small screen: 1 column without shrinking the image and with collapse navbar**
![sm_screen]

### Login, and Guest Login
![login]

### Posts Search
   * Search by username, group name, or post message
![search]

### User Profile
   * Display user's profile : about me, posts by user, and groups user joined
![profile]

### List of Groups, Posts, and Users
   * All Posts
![all_posts]

   * All Groups
![all_groups]

   * All Users
![all_users]

### Posts Pictures Preview
![post_preview]

### New Post/Group
![create_post]

[lg_screen]: ./assets/pics/lg_screen.png
[md_screen]: ./assets/pics/md_screen.png
[sm_screen]: ./assets/pics/sm_screen.png
[login]: ./assets/pics/login.png
[signup]: ./assets/pics/signup.png
[search]: ./assets/pics/search.png
[profile]: ./assets/pics/profile.png
[all_posts]: ./assets/pics/all_posts.png
[all_groups]: ./assets/pics/all_groups.png
[all_users]: ./assets/pics/all_users.png
[post_preview]: ./assets/pics/post_preview.png
[create_post]: ./assets/pics/create_post.png

## Implementation Timeline (2 weeks)

### Backend Setup,and User Authentication (2 days)

- [x] New Django project
- [x] Project setting
- [x] Project url router and views 
- [x] Default DB setting 
- [x] `User` model/migration
- [x] Inherit Django built-in authentication class
- [x] Basic Styling
- [x] Seed users
- [x] Navbar
- [x] Base templates
   
### `Accounts` App (1 day)

- [x] `Accounts` model creation
- [x] `Accounts` url routers
- [x] `Accounts` Class-Based Views (controller) 
- [x] `Accounts` model/migration 
- [x] `Accounts` Login/Sign Up html page templates

### `Posts` App (1 day)

- [x] `Posts` models creation
- [x] `Posts` url routers
- [x] `Posts` Class-Based Views (controller) 
- [x] `Posts` model/migration 
- [x] `Posts` CRUD html templates
- [x] Preview pictures modal function
- [x] Created links related to `Accounts`, `Posts` and `Groups` in post detail

### `Groups` App (1 day)
- [x] `Groups` models creation
- [x] `Groups` url routers
- [x] `Groups` Class-Based Views (controller) 
- [x] `Groups` model/migration 
- [x] `Groups` CRUD html templates
- [x] Join/Leave function and button
- [x] Counting icons of group members and posts

### Reviewing (1 day)

- [x] Reviewed new apps of `Accounts`, `Posts` and `Groups`
- [x] Bug fixes
- [x] Components styling using bootstrap 3
- [x] Seed data for database

### Fine Tuning Model Relationships (`Accounts`, `Posts` and `Groups`) (1 day)

- [x] Update foreign key/many-to-many fields for `Accounts`, `Posts` and `Groups`
- [x] Update url routers or buttons
- [x] Reviewing and Testing all functionality

### Posts Search (1 day)

- [x] Implemente post search for username, group name or post message 
- [x] Rendering related pages and adding the icon in the navbar

### User Profile and Guest Demo (1 day)

- [x] Profile template creation 
- [x] Implemented guest demo using JavaScript
- [x] All user list with thumbnail items 
- [x] Implemented counting icons for posts and groups

### Responsive Design (1 day)

- [x] Adjust Front End components with bootstrap grid system for responsive design
- [x] Styling navbar, posts templates, group templates, and user templates

### Masonry for Dynamic Listing Pictures (1 day)

- [x] Using Masonry package to list thumbnail images dynamically

### Deploying to Heroku (1 day)

- [x] Follow the Django-Python deployment instructions for deploying the project to Heroku


### Bonus Features (TBD)
- [ ] Follows of Users
- [ ] Likes for Posts

## Resources
Django:  
https://www.djangoproject.com/  

What is Django?  
<img src="https://www.filepicker.io/api/file/P6Z7Ac0UTVWr260Fvg7x" width=300 />  
image source: http://easylearning.guru   

Django FAQ:  
[Django appears to be a MVC framework, but you call the Controller the “view”, and the View the “template”. How come you don’t use the standard names?](https://docs.djangoproject.com/en/2.0/faq/general/)

 
