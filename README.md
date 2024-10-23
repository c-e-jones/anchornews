# Birmingham Anchor: A Local News Site Focused on the Birmingham Area
## A capstone project by Carl Jones

##  Project Description

### Base Concept

The base concept of this project was a simple full-stack development project, for which I designed the scope to be a simple news website focused on the local Birmingham area.

The name selected for this project was decided as the Birmingham Anchor. 


### Key Features

1. To provide a user authentication system, which allows users to log into the website and add records to the site.
2. CRUD functionality, which allows users to create, read, update and delete records added to the site. In the context of this website, it was simply a comment field, that allows users to discuss the news below the article in question, as well as edit or delete those comments / modify their review of the article.
3. Clearly understood structure, with clear content. This was achieved in this website by ensuring that content is neatly organised, in reverse chronological order, with tags for what genre of news the article fits into. This should provide an easily understood and navigable site design.
4. Responsivity - this site is designed with a mobile-first orientation, optimised primarily around being usable fully on any handheld device.


##  UX

The UX is intended to be as simple as feasibly possible, presenting the user with a simple news site design. 

### Users

The target audience of the site is users within the Birmingham area, seeking news and views about local issues and events. Due to this, most of the content on the website is tagged with locality in mind, with features looking to local government news, local events, wider regional events in the West Midlands area, and generally localised news. As most news sites can exist really without a national news section, there is also one of those. With this in mind, the target user for Birmingham Anchor is to provide an anchoring point to individuals in the West Midlands region who want local news and reporting, providing them a platform and ecosystem in which they can access and discuss news.

### Goals

The goal of this website is quite simplistic. It is to provide an easily read and understood centralized location for local reporting and discussion to be held about local events in the West Midlands region, but primarily Birmingham. Future feature concepts are the ability to actually sort articles by their genre category, to provide an average review score, and to enable users of the website to provide their own news articles to the site, transforming it from a news outlet into a news forum-blog structure. 


### User Stories

**Example 1**

> As a user, I would like to be able to view recent local news and to provide comment and view on the quality of it. If I make a mistake, I would like to be able to edit and correct it after the fact.
>
>     Users should be presented with a list view of the local news, which is sorted in reverse chronological order.
>     Users should be provided with the opportunity to add comments onto a new article, as well as a review.
>     If the user makes an error, they can edit it or even delete the comment. Feedback is provided to the user if they accidentally select delete, and a record is created of the edit being made and displayed to all users so they can keep track of edits.
>     

**Example 2**

> As a user, I do not like to read news which does not appeal to my interests. I would like to be able to sort and view news based on what type it is, so I can avoid reading news which isn't relevant to me.
>
>     A genre categorisation system should developed and deployed, which tells users which genre of news the article will discuss before they click onto it.
>     Future functionality will enable users to be able to sort the news by these genres, allowing them to more specifically get a list of personally preferred news and insights.

**Example 3**

> As a mobile phone user who does not own a desktop, I would like for the website to be usable on handheld devices.
>
>     The website should be openable and easily viewable in a responsive manner on mobile devices.
>     All UI elements must scale appropriately with these handheld restrictions, ensuring users are able to engage with the site appropriately and without suffering a negative user experience.

## AGILE Methodology

The development of this project used Agile tools in it's development, seeking to streamline the development process. Some of the key elements of this were **a kanban board and wireframing tools.**

### Kanban Board

To manage the workload of the task, I used the built in projects tools that GitHub provides, under the kanban tile view. For this, I added tasks as necessary, and moved them into appropriate categories as needed.
![image](https://github.com/user-attachments/assets/616565bd-5b1d-4c7a-9075-28e1c099567c)

### Wireframing

To conduct my basic wireframing, I used Balsamiq. Due to the simplicity of the website design, I only produced high quality wireframes.

****Index view / homepage****

![Wireframe 1](https://github.com/user-attachments/assets/13ea4e7f-72fa-429d-8dd6-e429e73d6ce5)

****Article view****

![Wireframe 2](https://github.com/user-attachments/assets/d4cecf28-979b-445a-b288-46854c3451ba)

****Comment fields****

![Wireframe 3](https://github.com/user-attachments/assets/a5924c77-68e6-4c37-8755-759b7bb5085c)

****Account management pages****

![Wireframe 4](https://github.com/user-attachments/assets/7eab2863-c5ed-49de-af01-a6f13e38b713)


### Colour Design

Colouring is an important element of any website, and should guide the user appropriately through their journey.

In the design of this website, five colours have been used. To help select colours, I have used Coolors, which is an online colour picking tool.

Initially, the design prospect was to brand this with a much closer visual identity to Birmingham. To achieve this, I intended to use the Birmingham flag colourway.

![image](https://github.com/user-attachments/assets/a369b545-e0f2-4c49-90db-484852978605)

However, as is often the case, colour patterns which work together well on a flag which exclusively uses symbology do not work quite as well together on a website with lots of text. In particular, every colour was too bright and too much of a primary colour, when what was necessary was to use softer hues which do not clash so heavily, and which provide effective contrast for text.

**Revised Colours**

![image](https://github.com/user-attachments/assets/ca0a6172-782f-4b2f-8e2b-199e96b025f3)

This new colour palette drops the yellow, as it did not work with any of the other colours selected, and the red was massively shifted down into being a warm white hue. Although much of the closer association to Birmingham colouring has been lost, this has made the website much less aggressive and garish.

The intent of future design is to refine the colouring down even further, and drill down to a closer 60-30-10 colour ruling. 

**Colours in practice**

![image](https://github.com/user-attachments/assets/0229b47a-db73-4919-ac7b-f8b9992e4791)

As shown above, the colours look like this on the site itself. The white is used as a contrast text colour to the blue colourway, while the grey-ebony colour is used as the contrast to the red. I opted for the grey over a pure black to soften the image of the site, and make it slightly less aggressive. The lighter shade of blue is only used on buttons. 

### Coding the Site

Before coding began, I needed to have a clear model in mind which relates entities to each other, and is customised to meet the task of my design. To achieve this, I used Lucidchart, and established a simple yet clear Entity Relationship Diagram. 

![ERD](https://github.com/user-attachments/assets/aca93875-2e2e-49e4-a386-f17ba797d962)

As shown above, this ERD connects the user as a Primary Key to the author categories in both the post and the comment models. This allows the application to track which user is the creator of what record.

The comment fields are themselves connected to the Title field as a foreign key, ensuring that comments are kept relevant to their specific post.

To provide some sort of feedback on whether content has been edited, I provided an edited status for both primary models, which is shown to the user as visual feedback beneath a post. This enables users to see visually whether anything has been altered after the fact.

### Code for the Models

****Post Model****

![image](https://github.com/user-attachments/assets/ba332bd8-6c5f-4c12-aaea-1401fcb11b0c)

In practice, this is what the Post model translates into. It has included help_text, to provide some basic user feedback and instruction of what they are supposed to be doing in a given field. Although this help model does not display anywhere on the frontend of the website yet, when user news contributions are made functional, this will automatically provide the user with these instructions as part of Summernote when that view and form is constructed. This prevents me having to migrate and potentially causing database issues down the line.

****Comment Model****

![image](https://github.com/user-attachments/assets/a24a90d5-c923-4861-a6e6-f470a323a5b7)

Likewise, the comment model also provides the same helptext. To organise the review choices slightly better, I produced these outside of the class, incase I decide to use them in a more complex way at a later date with a review aggregator class.

![image](https://github.com/user-attachments/assets/fbf33d96-e836-4d38-9fb8-0b5ee29b0590)


##  Testing Documentation

### Python Linter Testing

Many error instances of a line being too long are the result of Django base defaults. Any errors not a result of Django will be commented on directly.

**Settings**
![image](https://github.com/user-attachments/assets/78d45eb7-b7e2-4e60-844e-b8f66719c7f0)

These are primarily from urls and such, which do not impact functionality.

**urls.py (project)**

![image](https://github.com/user-attachments/assets/637e8606-9d4f-4619-bd1d-dce4698315ac)

**admin.py (app)**

![image](https://github.com/user-attachments/assets/daf5d800-4f70-4994-b84c-93e71ad2aa2a)

**forms.py (app)**

![image](https://github.com/user-attachments/assets/6564a96b-bd2f-4b28-942c-2d4714682a5c)

**models.py (app)**

![image](https://github.com/user-attachments/assets/0bdf4028-7d48-4689-a986-5f1923b03402)

As seen above, a number of errors were found on this file. However, all are rudimentary fixes due to a lack of new lines and lines which are too long.

![image](https://github.com/user-attachments/assets/4afff22e-7793-40de-aa94-c7170486728d)

**urls.py (app)**

![image](https://github.com/user-attachments/assets/c55c207a-764e-4a01-8093-26a7995f7862)

The same can be seen above. 

![image](https://github.com/user-attachments/assets/c376284a-dac6-4026-8dd9-dfd2eae254b2)

**views.py (app)**

![image](https://github.com/user-attachments/assets/aec4ea2f-23f5-4075-a41d-af4addbc5398)

Once more, a repetition of the same errors. Future code behaviour will need to reflect on the repetition of these errors.

![image](https://github.com/user-attachments/assets/4f0c0789-0df0-4c89-a9ce-0b6f4d5af388)

### HTML Validation

For the HTML validation, the W3 validator routinely flagged Django Markdown as errors. These have been hidden and any hidden errors are due to this, as 'fixing' them would break the website by causing data to not load.

**article.html**

![image](https://github.com/user-attachments/assets/89dec251-d3ab-4d22-ae7d-1cd3f10fbb46)

A stray div. 

![image](https://github.com/user-attachments/assets/f327807c-4ed2-4ca9-9764-9f420219ba7b)

**index.html**

![image](https://github.com/user-attachments/assets/c80301c6-42eb-4248-9169-36eb05df8202)

Another stray div, and copy-pasted hr spacing. 

![image](https://github.com/user-attachments/assets/c95c144e-74b6-431e-93a1-178bd4765b49)

**base.html**

![image](https://github.com/user-attachments/assets/191117e2-3f59-43cf-9dd9-cf8334c43846)

**login.html**

![image](https://github.com/user-attachments/assets/04479d8f-ee3b-48c2-9eb7-974d2431956d)

**logout.html**

![image](https://github.com/user-attachments/assets/9322f014-72e5-46b6-887b-6be3265a47e4)

**signup.html**

![image](https://github.com/user-attachments/assets/8dd1f799-89ec-4e7f-a6bc-827ef311d189)

### CSS Validation

![image](https://github.com/user-attachments/assets/067457f8-3488-428b-90b7-06feb943ed90)

As seen above, there is an error with the font weight being logged as a font-size instead. 

![image](https://github.com/user-attachments/assets/130617ad-ada4-4bd4-80a5-172ed517df65)

### Responsivity Testing

**Index**

![image](https://github.com/user-attachments/assets/5fb8215a-45dd-48e9-b370-de20779f048b)

![image](https://github.com/user-attachments/assets/a0de0394-4c48-4c15-944e-1166e47a0137)

No errors found, classified as a pass.

**Article View**

![image](https://github.com/user-attachments/assets/2e82437a-4b47-4905-bdad-e4b30c1b31c4)

![image](https://github.com/user-attachments/assets/2c79f916-0490-47cc-9bae-1c5d3993a50d)

**Logout**

![image](https://github.com/user-attachments/assets/e2162d64-8850-4594-b2e5-f93811ce8b75)

**Login**

![image](https://github.com/user-attachments/assets/34483bd7-263e-46e5-bdb0-7f8b8914c061)

**Register**

![image](https://github.com/user-attachments/assets/b46186cb-ae23-4db5-9557-0fbb95b10912)

Font sizes automatically adjust to a vw through a media query. These have been tested on a mobile device (Google Pixel 3A), and they are legible on all devices.

**Create account:** Pass
**Log In:** Pass
**Log Out:** Pass

**Can a user log into the admin panel with a non-superuser account?**

![image](https://github.com/user-attachments/assets/70a30400-23e3-43f8-9fab-b237ed5d3661)

No.

**Can a user that is signed in edit the records (in this case comments) of another user?**

![image](https://github.com/user-attachments/assets/92800fc3-463c-45e0-8bbf-ee0358977dba)

No. 

## Deployment

Version control for this app was conducted through GitHub. Coding was conducted using an IDE, in this instance Gitpod.

You can view the deployed model on [Heroku here.](https://anchor-news-f16076c85235.herokuapp.com)

Secret keys are connected to Config Vars in Heroku.

PostGres databse is connected via CodeInstitute.

You can create your own version of Birmingham Anchor thusly...

### Heroku (Step 1)

- Log into Heroku with a valid Heroku account
- Through Heroku, create a new app by clicking "New" on the dashboard, then "Create New App"
- Follow the instructions Heroku provides, selecting a unique name and a server region
- Click 'Create App'
- Connect your GitHub account to Heroku under "Deploy", selecting GitHub as the deployment method and connecting it to the GitHub repository

### Django (Step 1)

- Create your env.py file within the Django project. This should an independent file in the base - i.e., it should not be in any folders, at the topmost directory level.
- Open your .gitignore file, and add the env.py file to the list of ignored files. This prevents the information you are about to put into the env.py from being posted to your repository when you push any changes to the repo. 
- Configure your env.py file, importing the os, and setting up a SECRET_KEY and a DATABASE_URL.
- Complete the settings.py file, connecting it to the env.py by importing it and set it up to receive your now-hidden SECRET_KEY and DATABASE_URL.

### Heroku (Step 2)

- Return to the application in Heroku, and go to the Settings.
- Find your 'Config Vars', and reveal them.
- In the new field that is revealed to you, input your SECRET_KEY, DATABASE_URL and any other external dependencies such as Cloudinary if you are using that.
- You may also wish to include DISABLE_COLLECTSTATIC while editing your repo, and setting this to 1. If you do this, be sure to remove it before your final deployment.

### Django (Step 2)

- Back in Django, migrate your models.
- Go to your settings.py file and configure your static files, template directories and add Heroku to your ALLOWED_HOSTS.
- Create your Procfile within the Django project. This should also be an independent file in the base, at the topmost directory level.
- Configure your Procfile to run Gunicorn.

### Heroku (Step 3)

- Go to the 'Deploy' tab, and deploy the branch.
- If you have configured your repo correctly, this should deploy successfully. If not, check your errors and correct them in the repo.
- Once successfully deployed, it will link to the live project.
- Be sure to remove DISABLE_COLLECTSTATIC from your key:value pairs in Config Vars under settings. At this point, you should also ensure DEBUG is set to FALSE in your settings.py file. 

## Licencing Rights and Attributions, Credits and Thank Yous

Tools used:
- Django
- [Bootstrap](https://getbootstrap.com) (CC BY 3.0)
- [Font Awesome](https://fontawesome.com/v4/icons/) (CC BY 3.0)
- [Google Fonts](https://fonts.google.com) (SIL Open Font Licence)
- W3C Schools Linting tools and validators
- Heroku
- Cloudinary (however, it went unused)
- AllAuth
- Whitenoise
- Gunicorn

Due to an unfortunate series of mistakes, errors, and unfortunately timed life-events (allergic reaction), this project was restarted at a late minute. Due to this, some basic formatting and concepts were utilised based upon the "I Think Therefore I Blog" Code Institute tutorial. Where possible, changes have been made to aspects such as the model which was effectively rewritten, HTML, and the CSS. Although conceptually similar and similarly functioned, it is attempting to be distinct. Even getting this over the line was only made possible due to an extension, to which I must thank the Code Institute facilitators, particularly Lewis Dillon, for being understanding.

The failed project can be [viewed here.](https://github.com/c-e-jones/birmingham-anchor) 

The above project will be returned to with fresh eyes, in an attempt to make a pseudo-GIS project.

Although not used in this project, I would also like to thank [Ryan Chung](https://www.youtube.com/watch?v=65flD9ScEQM&t=243s) for providing good instructions and demonstration of incorporating Mapbox into Django. In the previous failed project, this is what motivated me to make the attempt. The errors in that project were all my own.
