// @ts-check
import { defineConfig, fontProviders } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	// Fonts are downloaded at build time and served from this site,
	// so visitors never make requests to Google.
	fonts: [
		{
			// Headings. Variable font with weight and optical size (opsz) axes.
			name: 'Fraunces',
			cssVariable: '--font-serif',
			provider: fontProviders.google(),
			weights: ['400 700'],
			styles: ['normal'],
			subsets: ['latin'],
			fallbacks: ['Georgia', 'serif'],
			options: {
				experimental: { variableAxis: { opsz: [['9', '144']] } },
			},
		},
		{
			// Body text.
			name: 'Inter',
			cssVariable: '--font-sans',
			provider: fontProviders.google(),
			weights: ['400 600'],
			styles: ['normal'],
			subsets: ['latin'],
			fallbacks: ['system-ui', 'sans-serif'],
		},
	],
});
