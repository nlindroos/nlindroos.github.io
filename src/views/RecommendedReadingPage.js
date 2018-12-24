import React, { Component } from 'react';
import { get } from 'lodash';
// import Select from 'react-select';
import Autosuggest from 'react-autosuggest';
import TextField from '@material-ui/core/TextField';
// import '../styles/about-page.css';

const recommendedReading = [
  {
    title: 'hey',
    link: 'hey1',
  },
  {
    title: 'yo',
    link: 'yo1',
  },
];
// ].map(({ title }) => ({ value: title, label: title }));

const getSuggestions = filter => {
  const inputValue = filter.trim().toLowerCase();
  const inputLength = inputValue.length;

  if (inputLength === 0) {
    return recommendedReading;
  }
  return recommendedReading.filter(resource => resource.title.toLowerCase().slice(0, inputLength) === inputValue);
};

const renderSuggestion = suggestion => <div>{suggestion.title}</div>;

const renderInput = props => <TextField fullWidth {...props} />;

const getSuggestionValue = suggestion => get(suggestion, 'title', '');
class RecommendedReadingPage extends Component {
  state = {
    filter: '',
    suggestions: recommendedReading,
  };

  componentDidMount() {
    // @@TODO Fetch articles
  }

  handleChange = (event, { newValue: filter }) => {
    this.setState({ filter });
  };

  handleSuggestionsFetchRequested = ({ value }) => {
    this.setState({
      suggestions: getSuggestions(value),
    });
  };

  handleSuggestionsClearRequested = () => {
    this.setState({
      suggestions: [],
    });
  };

  render() {
    const { filter, suggestions } = this.state;

    const inputProps = {
      placeholder: 'Just start typing',
      value: filter,
      onChange: this.handleChange,
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
        />
      </div>
    );
  }
}

export default RecommendedReadingPage;
