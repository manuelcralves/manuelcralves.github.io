import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// One Markdown file per project in src/content/projects.
// A missing or malformed field fails the build instead of shipping a broken page.
const projects = defineCollection({
	loader: glob({ pattern: '*.md', base: './src/content/projects' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			summary: z.string().max(200),
			order: z.number().int().positive(),
			kind: z.string(),
			period: z.string(),
			stack: z.array(z.string()).min(1),
			team: z.array(z.string()).optional(),
			highlight: z.object({ value: z.string(), label: z.string() }).optional(),
			links: z.array(z.object({ label: z.string(), href: z.url() })).default([]),
			// One drawing per entry, in a light and a dark version.
			diagrams: z
				.array(
					z.object({
						// Completes the link text for screen readers: "Open the full drawing of ...".
						name: z.string(),
						light: image(),
						dark: image(),
						alt: z.string(),
						caption: z.string(),
					})
				)
				.default([]),
		}),
});

export const collections = { projects };
