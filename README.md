## Django Blog Project

### This is a simple blog project created using Django. It includes the following features:

    Create, edit, and delete blog posts
    Manage categories and tags
    Add comments to blog posts
    Search blog posts
    View recent posts
    View a list of all posts

### Getting Started

To get started, you will need to install the following:

    Python 3
    Pip
    Virtualenv
    Django

### Once you have installed all of the requirements, you can clone this repository and create a virtual environment:

git clone https://github.com/dhiraj1008/django_projects.git
cd django-blog-project
python3 -m venv env
source env/bin/activate

### Once you have activated the virtual environment, you can install the project dependencies:

pip install -r requirements.txt

### Running the Project

To run the project, simply execute the following command:

python manage.py runserver

This will start the Django development server on port 8000. You can then open your web browser and navigate to http://localhost:8000/ to view the blog.

### Creating a Superuser

Before you can start creating blog posts, you will need to create a superuser account. To do this, run the following command:

python manage.py createsuperuser

You will be prompted to enter a username, email address, and password.

### Adding Blog Posts

To add a blog post, navigate to the admin interface at /admin/. Once you are logged in, click on the "Posts" link.

On the blog post list page, click on the "Add" button to create a new blog post.

Enter a title, slug, and body content for the blog post. You can also add categories, tags, and an image to the blog post.

Once you are finished creating the blog post, click on the "Save" button.

### Viewing Blog Posts

To view all of the blog posts, navigate to the blog home page at /.

To view a specific blog post, click on the title of the post.

### Adding Comments to Blog Posts

To add a comment to a blog post, navigate to the blog post page and scroll down to the comments section.

Enter your name, email address, and comment text.

Once you are finished writing your comment, click on the "Submit Comment" button.

### Searching Blog Posts

To search for blog posts, enter a search term in the search bar at the top of the page and press Enter.

The search results will display all of the blog posts that match the search term.

### Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

Before submitting a pull request, please make sure that you have added tests to cover your changes.

#### Be Kind :)
