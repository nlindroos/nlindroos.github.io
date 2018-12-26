import Contentful from '../services/contentfulClient';

export const types = {
  FETCHING_RECOMMENDED: 'CONTENTFUL/FETCHING_RECOMMENDED',
  FETCHING_RECOMMENDED_FAILURE: 'CONTENTFUL/FETCHING_RECOMMENDED_FAILURE',
  FETCHING_RECOMMENDED_SUCCESS: 'CONTENTFUL/FETCHING_RECOMMENDED_SUCCESS',
};

export const getRecommendedReading = () => async dispatch => {
  dispatch({ type: types.FETCHING_RECOMMENDED });
  try {
    const recommendedReading = await Contentful.getRecommendedReading();

    // console.log('recommendedReading', recommendedReading);
    // await new Promise(resolve => setTimeout(resolve, 4000));

    dispatch({
      type: types.FETCHING_RECOMMENDED_SUCCESS,
      payload: {
        recommendedReading,
      },
    });
  } catch (e) {
    dispatch({ type: types.FETCHING_RECOMMENDED_FAILURE });
  }
};
