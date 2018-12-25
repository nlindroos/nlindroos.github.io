import Contentful from '../services/contentfulClient';

export const types = {
  GET_RECOMMENDED_READING: 'CONTENTFUL_GET_RECOMMENDED_READING',
};

export const getRecommendedReading = () => async () => {
  const articles = await Contentful.getRecommendedReading();

  //   console.log('articles', articles);
  return {
    type: types.GET_RECOMMENDED_READING,
    payload: {
      articles,
    },
  };
};
