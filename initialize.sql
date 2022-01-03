\connect postgres

drop database if exists tp;
create database tp;

\connect tp

\i create.sql

\copy Users(user_id,date_created,password,first_name,last_name,date_of_birth,ethnicity)     FROM 'csvfiles/User.csv' csv header
\copy Monetized_User(user_id)                                                               FROM 'csvfiles/Monetized_User.csv' csv header
\copy Normal_User(user_id)                                               FROM 'csvfiles/Normal_User.csv' csv header
\copy Company(user_id,company_name)                                      FROM 'csvfiles/Company.csv' csv header
\copy Story(story_id,user_id,interaction_count)                                   FROM 'csvfiles/Story.csv'    csv header
\copy Post(post_id,user_id)                                                      FROM 'csvfiles/Post.csv'    csv header
\copy Monetized_Post(post_id,money_made)                                 FROM 'csvfiles/Monetized_Post.csv'    csv header
\copy Comment(comment_id,message,user_id,post_id)                                   FROM 'csvfiles/Comment.csv'     csv header
\copy Follows(user_id1,user_id2,date_followed)                           FROM 'csvfiles/Follows.csv'    csv header



