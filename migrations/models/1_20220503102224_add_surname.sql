-- upgrade --
ALTER TABLE "countries" ADD "surname" VARCHAR(111) NOT NULL;
-- downgrade --
ALTER TABLE "countries" DROP COLUMN "surname";
