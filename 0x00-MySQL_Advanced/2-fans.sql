-- Solve a sorting problem
-- Select statement to select and group results

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
