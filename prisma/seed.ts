import { PrismaClient } from '@prisma/client';
import { readFileSync } from 'fs';

const words: Word[] = JSON.parse(
  readFileSync(new URL('./total_words.json', import.meta.url), 'utf-8')
);


const prisma = new PrismaClient();

interface Word {
  english: string;
  partOfSpeech: string;
  chinese: string;
}

// const words: Word[] = data.map(({ english, translate, part_of_speech }) => ({
//   english: english,
//   partOfSpeech: part_of_speech,
//   chinese: translate
// }));

async function main() {
  // Seed Words
  await prisma.word.deleteMany({});

  await prisma.word.createMany({
    data: words,
  });

  console.log("Database seeded!");
}

main()
  .catch((e) => console.error(e))
  .finally(async () => {
    await prisma.$disconnect();
  });
