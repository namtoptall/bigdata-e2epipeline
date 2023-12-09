use kafkapipeline;
create table if not exists kafkapipeline.fakerdaata(
    name text, 
    address text, 
    phone text,
    job text,
    email text,
    copmany text,
    country text, primary key(name, adrress)
);



