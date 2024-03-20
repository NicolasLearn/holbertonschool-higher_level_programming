-- Task 11
-- Lists all shows contained in 'hbtn_0d_tvshows' without a genre linked.
SELECT sh.`title`, sg.`genre_id`
    FROM `tv_shows` AS sh
    LEFT JOIN `tv_show_genres` AS sg
    ON sh.`id` = sg.`show_id`
    WHERE sg.`genre_id` IS NULL
    ORDER BY sh.`title`, sg.`genre_id`;
