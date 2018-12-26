import { createClient } from 'contentful';

import { CONTENT_TYPES } from '../constants/contentfulConstants';

const formatEntries = entries =>
  entries.map(({ fields }) => ({
    ...fields,
    // Conditionally add tags
    ...(fields.tags && { tags: fields.tags.map(tag => tag.fields.name) }),
    type: fields.type.fields.name,
  }));

// Utilising both @babel/plugin-proposal-optional-chaining
// and @babel/plugin-proposal-nullish-coalescing-operator
// ({...(entry?.fields ?? {}), ...(entry?.fields?.tags && {tags: entry?.fields?.tags.})}));

class Contentful {
  initialised = false;

  client = null;

  initialise = () => {
    this.client = createClient({
      space: process.env.CONTENTFUL_SPACE,
      accessToken: process.env.CONTENTFUL_ACCESS_TOKEN,
    });
    this.initialised = true;
  };

  getRecommendedReading = async () => {
    if (!this.initialised) {
      this.initialise();
    }
    const recommended = await this.client.getEntries({
      content_type: CONTENT_TYPES.RECOMMENDED,
    });

    return formatEntries(recommended.items);
  };
}

export default new Contentful();
