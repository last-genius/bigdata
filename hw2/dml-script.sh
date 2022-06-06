#!/bin/bash

QUERY="
  USE hw2_sultanov;

  INSERT INTO favorite_songs( id, author, song_name, release_year) VALUES (1, 'Morwan', 'Зола-Земля', 2020);
  INSERT INTO favorite_songs( id, author, song_name, release_year) VALUES (2, 'G.L.O.S.S.', 'Lined Lips and Spiked Bats', 2016);

  INSERT INTO favorite_movies ( id, name, producer, release_year) VALUES (1, 'Andrei Rublev', 'Andrei Tarkovsky', 1966);
  INSERT INTO favorite_movies ( id, name, producer, release_year) VALUES (2, 'Persona', 'Ingmar Bergman', 1966);
  
  SELECT * FROM favorite_songs;
  SELECT * FROM favorite_movies;
  "

docker exec -it cassandra-node1 cqlsh -e "${QUERY}"
