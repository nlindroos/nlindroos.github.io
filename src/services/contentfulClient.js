import { createClient } from 'contentful';

import { CONTENT_TYPES } from '../constants/contentfulConstants';

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
    const recommended = await this.client.getContentType(CONTENT_TYPES.RECOMMENDED);

    return recommended.toPlainObject();
  };
}

export default new Contentful();
