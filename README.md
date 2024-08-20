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

All links function as detail lists above.

### Homepage


### CSS


### Python Code


  
## Licencing Rights and Attributions

For the construction of this website, we have used a number of assets which are not made by ourselves. They are, however, covered by Open Source licencing, and are fair use under a Creative Commons licence.

Tools used:
- [Bootstrap](https://getbootstrap.com) (CC BY 3.0)
- [Font Awesome](https://fontawesome.com/v4/icons/) (CC BY 3.0)
- [Google Fonts](https://fonts.google.com) (SIL Open Font Licence)
- [Pexels](https://www.pexels.com) (CC0)

## 9. Other Documents
