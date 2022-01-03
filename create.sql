-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-12-06 01:29:52.376

-- tables
-- Table: Comment
CREATE TABLE Comment (
    comment_id int  NOT NULL,
    message text  NOT NULL,
    user_id int  NOT NULL,
    post_id int  NOT NULL,
    CONSTRAINT Comment_pk PRIMARY KEY (comment_id)
);

-- Table: Company
CREATE TABLE Company (
    user_id int  NOT NULL,
    company_name text  NOT NULL,
    CONSTRAINT Company_pk PRIMARY KEY (user_id)
);

-- Table: Follows
CREATE TABLE Follows (
    user_id1 int  NOT NULL,
    user_id2 int  NOT NULL,
    date_followed date  NOT NULL,
    CONSTRAINT Follows_pk PRIMARY KEY (user_id1)
);

-- Table: Monetized_Post
CREATE TABLE Monetized_Post (
    post_id int  NOT NULL,
    money_made int  NOT NULL,
    CONSTRAINT Monetized_Post_pk PRIMARY KEY (post_id)
);

-- Table: Monetized_User
CREATE TABLE Monetized_User (
    user_id int  NOT NULL,
    CONSTRAINT Monetized_User_pk PRIMARY KEY (user_id)
);

-- Table: Normal_User
CREATE TABLE Normal_User (
    user_id int  NOT NULL,
    CONSTRAINT Normal_User_pk PRIMARY KEY (user_id)
);

-- Table: Post
CREATE TABLE Post (
    post_id int  NOT NULL,
    user_id int  NOT NULL,
    CONSTRAINT Post_pk PRIMARY KEY (post_id)
);

-- Table: Story
CREATE TABLE Story (
    story_id int  NOT NULL,
    user_id int  NOT NULL,
    interaction_count int  NOT NULL,
    CONSTRAINT Story_pk PRIMARY KEY (story_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id int  NOT NULL,
    date_created date  NOT NULL,
    password text  NOT NULL,
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    date_of_birth date  NOT NULL,
    ethnicity text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Comment_Post (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT Comment_Post
    FOREIGN KEY (post_id)
    REFERENCES Post (post_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comment_User (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT Comment_User
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Company_User (table: Company)
ALTER TABLE Company ADD CONSTRAINT Company_User
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Followed_User (table: Follows)
ALTER TABLE Follows ADD CONSTRAINT Followed_User
    FOREIGN KEY (user_id2)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Follows_User (table: Follows)
ALTER TABLE Follows ADD CONSTRAINT Follows_User
    FOREIGN KEY (user_id1)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Monetized_User_User (table: Monetized_User)
ALTER TABLE Monetized_User ADD CONSTRAINT Monetized_User_User
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Normal_User_User (table: Normal_User)
ALTER TABLE Normal_User ADD CONSTRAINT Normal_User_User
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Post_Monetized_Post (table: Monetized_Post)
ALTER TABLE Monetized_Post ADD CONSTRAINT Post_Monetized_Post
    FOREIGN KEY (post_id)
    REFERENCES Post (post_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Post_User (table: Post)
ALTER TABLE Post ADD CONSTRAINT Post_User
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Story_User (table: Story)
ALTER TABLE Story ADD CONSTRAINT Story_User
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

