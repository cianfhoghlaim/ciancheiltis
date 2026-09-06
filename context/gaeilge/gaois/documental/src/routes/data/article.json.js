import { getArticle, listArticles } from './_article';
import { listVersions } from './_versions';
import { errorMessage } from 'utils/messenger';

export function get(req, res) {
	const { locale, category, resource, version, slug } = req.query;

	let dir = `docs/${category}/${resource}`;
	let versions;
	let articles;

	if (!!version) {
		versions = listVersions(dir);
		dir += `/${version}`;
	}

	const filePath = (!!slug) ? `${dir}/${slug}.${locale}.md` : `${dir}/index.${locale}.md`;
	const alternateLocale = (locale === 'en') ? 'ga' : 'en';
	const alternateFilePath = (!!slug) ? `${dir}/${slug}.${alternateLocale}.md` : `${dir}/index.${alternateLocale}.md`;
	const { file, monolingual } = getArticle(filePath, alternateFilePath);

	articles = listArticles(dir, locale, alternateLocale);

	if (file) {
		res.writeHead(200, {
			'Content-Type': 'application/json'
		});

		let result = {};
		result.markdown = file;
		result.monolingual = monolingual;
		result.versions = versions;
		result.articles = articles;

		res.end(JSON.stringify(result));
	} else {
		res.writeHead(404, {
			'Content-Type': 'application/json'
		});

		res.end(JSON.stringify({
			message: errorMessage(404, locale)
		}));
	}
};