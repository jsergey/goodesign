create table commits (
    author          text,
    hash            text,
    commit_date     date,
    file            text,
    file_path       text,
    added           integer,
    removed         integer
);