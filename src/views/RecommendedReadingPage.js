import { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Autosuggest from 'react-autosuggest';
import TextField from '@material-ui/core/TextField';
import Fuse from 'fuse.js';
import styled from 'react-emotion';

import { getRecommendedReading } from '../actions/contentfulActions';
import RecommendedReadingRow from '../containers/RecommendedReadingRow';
import FullScreenLoader from '../components/FullScreenLoader';
// import '../styles/about-page.css';

// const getSuggestions = filter => {
//   const inputValue = filter.trim().toLowerCase();
//   const inputLength = inputValue.length;

//   if (inputLength === 0) {
//     return recommendedReading;
//   }
//   return recommendedReading.filter(resource => resource.title.toLowerCase().slice(0, inputLength) === inputValue);
// };

const fuseOptions = {
  shouldSort: true,
  threshold: 0.4,
  location: 0,
  distance: 100,
  maxPatternLength: 12,
  minMatchCharLength: 1,

  // tokenize: true,
  // findAllMatches: true,
  // includeMatches: true,
  keys: [
    // 'tags',
    // 'title',
    {
      name: 'tags',
      weight: 0.7,
    },
    {
      name: 'title',
      weight: 0.3,
    },
    // {
    //   name: 'authors',
    //   weight: 0.2,
    // },
  ],
};

const SuggestionsContainer = styled.div`
  ul {
    padding-inline-start: 0px;
  }
`;

const renderSuggestionsContainer = ({ containerProps, children }) => (
  <SuggestionsContainer {...containerProps}>{children}</SuggestionsContainer>
);

const renderSuggestion = suggestion => <RecommendedReadingRow resource={suggestion} />;

const renderInput = ({ ref, ...rest }) => (
  <TextField
    fullWidth
    {...rest}
    InputProps={{
      // Pass the correct ref to react-autosuggest
      inputRef: _ => ref(_),
    }}
  />
);

const getSuggestionValue = suggestion => suggestion?.title ?? '';

class RecommendedReadingPage extends Component {
  state = {
    filter: '',
    suggestions: [],
  };

  fuse = null;

  componentDidMount() {
    this.props.getRecommendedReading();
  }

  componentDidUpdate(prevProps) {
    const { recommended } = this.props;

    if (recommended.length > prevProps.recommended.length) {
      this.setState({ suggestions: recommended });
      this.fuse = new Fuse(recommended, fuseOptions);
    }
  }

  getSuggestions = filter => this.fuse.search(filter);
  // .map(result => {
  //   // console.log('result', result);
  //   return result;
  //   // return result.item;
  // });

  handleChange = (event, { newValue: filter }) => {
    this.setState({ filter });
  };

  handleSuggestionsFetchRequested = ({ value }) => {
    const { recommended } = this.props;

    this.setState({
      suggestions: value ? this.getSuggestions(value) : recommended,
    });
  };

  handleSuggestionsClearRequested = () => {
    this.setState({
      filter: '',
      suggestions: this.props.recommended,
    });
  };

  render() {
    const { filter, suggestions } = this.state;
    const { fetching } = this.props;

    const inputProps = {
      placeholder: 'Just start typing a title or topic',
      value: filter,
      onChange: this.handleChange,
      InputLabelProps: {
        shrink: true,
      },
    };

    return (
      <div>
        <h2 className="alt-header">Recommended reading</h2>

        {/* <AutoSuggestInput filter={filter} suggestions={suggestions}  /> */}
        <Autosuggest
          alwaysRenderSuggestions
          suggestions={suggestions}
          onSuggestionsFetchRequested={this.handleSuggestionsFetchRequested}
          onSuggestionsClearRequested={this.handleSuggestionsClearRequested}
          getSuggestionValue={getSuggestionValue}
          renderSuggestion={renderSuggestion}
          inputProps={inputProps}
          renderInputComponent={renderInput}
          renderSuggestionsContainer={renderSuggestionsContainer}
        />
        <FullScreenLoader loading={fetching} />
      </div>
    );
  }
}

RecommendedReadingPage.propTypes = {
  fetching: PropTypes.bool.isRequired,
  getRecommendedReading: PropTypes.func.isRequired,
  recommended: PropTypes.arrayOf(PropTypes.shape()).isRequired,
};

const mapStateToProps = ({ contentful }) => ({
  fetching: contentful.fetching,
  recommended: contentful.recommendedReading,
});

const mapDispatchToProps = {
  getRecommendedReading,
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecommendedReadingPage);
