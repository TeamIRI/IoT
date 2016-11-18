SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS hourly_tmp_hum (
  id int(11) NOT NULL,
  updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  station_id int(11) NOT NULL,
  mintmp float DEFAULT NULL,
  avgtmp float DEFAULT NULL,
  maxtmp float DEFAULT NULL,
  minhum float DEFAULT NULL,
  avghum float DEFAULT NULL,
  maxhum float DEFAULT NULL,
  numsamp int(11) NOT NULL DEFAULT '0',
  timesamp timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
);

ALTER TABLE hourly_tmp_hum
  ADD PRIMARY KEY (id), ADD KEY timesamp (timesamp);

ALTER TABLE hourly_tmp_hum
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;
