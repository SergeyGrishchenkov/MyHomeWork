CREATE TABLE table_my
(
key INTEGER PRIMARY KEY AUTOINCREMENT,
short_name CHAR(50) NOT NULL,
full_name CHAR(200) NOT NULL,
desc CHAR(512),
loc_id INT NOT NULL,
FOREIGN KEY(loc_id) REFERENCES locations(location_id)
);
--****************************
ALTER TABLE table_my RENAME TO just_table;
--****************************
ALTER TABLE just_table ADD status CHAR(20);
--****************************
INSERT INTO just_table
(short_name, full_name, desc, loc_id, status)
VALUES
('test1','My test1','Desc of My test1', 1000, 'on sale');
--****************************
INSERT INTO just_table
(short_name, full_name, desc, loc_id, status)
VALUES
('test2','My test2','Desc of My test2', 1200, 'reserved');
--****************************
select * from just_table;
--****************************
UPDATE just_table
SET status = 'on sale'
WHERE short_name = 'test2';
--****************************
select * from just_table;
--****************************
DELETE FROM just_table
WHERE loc_id = 1200;
--****************************
select * from just_table;
--****************************