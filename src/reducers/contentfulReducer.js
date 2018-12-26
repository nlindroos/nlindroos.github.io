import { types } from '../actions/contentfulActions';

const initialState = {
  fetching: false,
  fetchingFailed: false,
  recommendedReading: [],
};

const contentfulReducer = (state = initialState, action) => {
  const { type, payload = {} } = action;
  switch (type) {
    case types.FETCHING_RECOMMENDED:
      return {
        ...state,
        fetching: true,
      };
    case types.FETCHING_RECOMMENDED_SUCCESS:
      return {
        ...state,
        ...payload,
        fetching: false,
        fetchingFailed: false,
      };
    case types.FETCHING_RECOMMENDED_FAILURE:
      return {
        ...state,
        fetching: false,
        fetchingFailed: true,
      };
    // case types.FETCHING_RECOMMENDED:
    //   return {
    //     ...state,
    //     ...payload,
    //   };
    default:
      return state;
  }
};

export default contentfulReducer;
