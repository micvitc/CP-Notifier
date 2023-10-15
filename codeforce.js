const axios = require('axios');
const cheerio = require('cheerio');

async function scrapePage(pageNo) {
  const url = 'https://codeforces.com/problemset/page/' + pageNo.toString();

  try {
    const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

    const problems = $('.problems tbody tr');

    problems.each((index, element) => {
      const title = $(element).find('td:eq(1)').text().trim();
      const link = 'https://codeforces.com' + $(element).find('td:eq(0) a').attr('href');
      console.log('Title:', title);
      console.log('Link:', link);
    });

    // Introduce a delay before the next request
    await new Promise(resolve => setTimeout(resolve, 1000)); // 1-second delay
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function scrapePages() {
  for (let pageNo = 1; pageNo <= 89; pageNo++) {
    await scrapePage(pageNo);
  }
}

scrapePages();