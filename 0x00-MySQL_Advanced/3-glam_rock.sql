-- Old school band
-- get the lifespan of Glam rock bands
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan from `metal_bands` WHERE `style` LIKE '%Glam rock%'
