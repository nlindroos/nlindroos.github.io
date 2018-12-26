import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { get } from 'lodash';
// import Select from 'react-select';
import Autosuggest from 'react-autosuggest';
import TextField from '@material-ui/core/TextField';

import { getRecommendedReading } from '../actions/contentfulActions';
// import '../styles/about-page.css';

// const recommendedReading = [
//   {
//     title: 'hey',
//     link: 'hey1',
//   },
//   {
//     title: 'yo',
//     link: 'yo1',
//   },
// ];
// ].map(({ title }) => ({ value: title, label: title }));

// const getSuggestions = filter => {
//   const inputValue = filter.trim().toLowerCase();
//   const inputLength = inputValue.length;

//   if (inputLength === 0) {
//     return recommendedReading;
//   }
//   return recommendedReading.filter(resource => resource.title.toLowerCase().slice(0, inputLength) === inputValue);
// };

const renderSuggestion = suggestion => <div>{suggestion.title}</div>;

const renderInput = props => <TextField fullWidth {...props} />;

const getSuggestionValue = suggestion => get(suggestion, 'title', '');

class RecommendedReadingPage extends Component {
  state = {
    filter: '',
    suggestions: [],
  };

  componentDidMount() {
    this.props.getRecommendedReading();
  }

  getSuggestions = filter => {
    const { recommended } = this.props;
    const inputValue = filter.trim().toLowerCase();
    const inputLength = inputValue.length;

    if (inputLength === 0) {
      return recommended;
    }
    return recommended.filter(resource => resource.title.toLowerCase().slice(0, inputLength) === inputValue);
  };

  handleChange = (event, { newValue: filter }) => {
    this.setState({ filter });
  };

  handleSuggestionsFetchRequested = ({ value }) => {
    this.setState({
      suggestions: this.getSuggestions(value),
    });
  };

  handleSuggestionsClearRequested = () => {
    // console.log('clear');
    this.setState({
      suggestions: [],
    });
  };

  render() {
    const { filter, suggestions } = this.state;
    const { fetching } = this.props;

    const inputProps = {
      placeholder: 'Just start typing a title or topic',
      value: filter,
      onChange: this.handleChange,
    };

    if (fetching) {
      return <p>fetching</p>;
    }

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
        />
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
