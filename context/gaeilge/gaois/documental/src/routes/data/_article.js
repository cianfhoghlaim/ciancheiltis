import fs from 'fs';
import { parseMarkdown } from 'utils/markdown';

const getArticle = (filePath, alternateFilePath) => {
	let file;
	let monolingual = false;

	if (fs.existsSync(filePath)) {
		file = fs.readFileSync(filePath, 'utf-8');
        
        const { content } = parseMarkdown(file);

        if (!content && fs.existsSync(alternateFilePath)) {
            file = fs.readFileSync(alternateFilePath, 'utf-8');
            monolingual = true;
        }
	} else if (fs.existsSync(alternateFilePath)) {
		file = fs.readFileSync(alternateFilePath, 'utf-8');
		monolingual = true;
    }
    
    return { file, monolingual };
};

const listArticles = (path, locale, alternateLocale) => {
    let slugs = [];
    let articles = [];
    let result = [];

    fs.readdirSync(path)
        .filter(file => file[0] !== '.' && /[^\\]*\.(md)$/.test(file))
        .map(file => {
            const slug = file.slice(0, -6);
            
            if (!slugs.includes(slug)) slugs.push(slug);

            const locale = file.slice(file.length - 5, -3);
            const markdown = fs.readFileSync(`${path}/${file}`, 'utf-8');

            if (!!markdown) {
                const { metadata } = parseMarkdown(markdown);
                articles.push({ slug: slug, locale: locale, ...metadata });
            }
        });

    articles.filter(article => {
        if (article.locale === locale) {
            result.push(article);
        }
    });

    for (const slug of slugs) {
        if (!result.find(article => article.slug === slug)) {
            const articleAlternate = articles.find(article => article.slug === slug && article.locale === alternateLocale);
            if (articleAlternate) result.push(articleAlternate);
        }
    }

    result.sort((a, b) => {
        if (!!a.order && !!b.order) {
            return a.order - b.order
        } else if (!!a.order && !b.order) {
            return -1;
        } else if (!a.order && !!b.order) {
            return 1;
        } else {
            return a.title.localeCompare(b.title);
        }
    });

    return result;
};

export { getArticle, listArticles };