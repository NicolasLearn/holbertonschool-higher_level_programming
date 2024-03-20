-- Task 16
-- Lists all shows, and all genres linked to that show, from the database 'hbtn_0d_tvshows'.
SELECT sh.`title`, gen.`name`
    FROM `tv_shows` AS sh
        LEFT JOIN `tv_show_genres` AS sg
        ON sh.`id` = sg.`show_id`
        LEFT JOIN `tv_genres` AS gen
        ON sg.`genre_id` = gen.`id`
    ORDER BY sh.`title`, gen.`name`;
