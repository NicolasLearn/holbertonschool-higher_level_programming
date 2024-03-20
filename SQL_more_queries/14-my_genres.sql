-- Task 14
-- Uses the 'hbtn_0d_tvshows' database to lists all genres of the show 'Dexter'.
SELECT gen.`name`
    FROM `tv_genres` AS gen
        INNER JOIN `tv_show_genres` AS sg
        ON gen.`id` = sg.`genre_id`
        INNER JOIN `tv_shows` AS t
        ON t.`id` = sg.`show_id`
        WHERE t.`title` = "Dexter"
    ORDER BY gen.`name`;
