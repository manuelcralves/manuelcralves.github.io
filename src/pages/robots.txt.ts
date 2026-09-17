import type { APIRoute } from 'astro';

// Written from the site URL in astro.config.mjs, so it cannot fall out of date.
export const GET: APIRoute = ({ site }) => {
	const body = `User-agent: *
Allow: /

Sitemap: ${new URL('sitemap-index.xml', site)}
`;
	return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
