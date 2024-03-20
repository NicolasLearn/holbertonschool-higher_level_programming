-- Task 14
-- Uses the 'hbtn_0d_tvshows' database to lists all genres of the show 'Dexter'.
SELECT sh.`title`
    FROM `tv_shows` AS sh
        INNER JOIN `tv_show_genres` AS sg
        ON sh.`id` = sg.`show_id`
        INNER JOIN `tv_genres` AS gen
        ON gen.`id` = sg.`genre_id`
       WHERE gen.`name` = "Comedy"
    ORDER BY sh.`title`;
