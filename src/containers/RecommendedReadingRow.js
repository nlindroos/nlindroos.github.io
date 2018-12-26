import PropTypes from 'prop-types';
import styled from 'react-emotion';

// import colours from '../constants/colours';

const RowContainer = styled.div`
  flex-grow: 1;
`;

const RecommendedReadingRow = ({ resource }) => <RowContainer>{resource.title}</RowContainer>;

RecommendedReadingRow.propTypes = {
  resource: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string,
    tags: PropTypes.arrayOf(PropTypes.string),
  }).isRequired,
};
export default RecommendedReadingRow;
