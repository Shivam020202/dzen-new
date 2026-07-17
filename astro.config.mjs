import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // TODO(checkpoint): confirm production domain — placeholder until provided
  site: 'https://dzenderma.com',
  trailingSlash: 'never',
  build: {
    inlineStylesheets: 'auto',
  },
});
