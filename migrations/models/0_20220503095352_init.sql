-- upgrade --
CREATE TABLE IF NOT EXISTS "countries" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "iso" VARCHAR(3) NOT NULL,
    "icon" TEXT NOT NULL,
    "is_active" BOOL NOT NULL,
    "additional_info" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
