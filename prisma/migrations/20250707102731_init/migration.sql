/*
  Warnings:

  - You are about to drop the column `audio` on the `Word` table. All the data in the column will be lost.

*/
-- RedefineTables
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Word" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "english" TEXT NOT NULL,
    "partOfSpeech" TEXT NOT NULL,
    "chinese" TEXT NOT NULL,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "new_Word" ("chinese", "createdAt", "english", "id", "partOfSpeech") SELECT "chinese", "createdAt", "english", "id", "partOfSpeech" FROM "Word";
DROP TABLE "Word";
ALTER TABLE "new_Word" RENAME TO "Word";
CREATE UNIQUE INDEX "Word_english_partOfSpeech_key" ON "Word"("english", "partOfSpeech");
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;
