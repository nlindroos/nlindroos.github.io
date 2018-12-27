import PropTypes from 'prop-types';
import styled from 'react-emotion';

import Tag from '../components/Tag';

const Container = styled.div`
  display: flex;
  flex-direction: row;
`;

const TagContainer = ({ tags }) => (
  <Container>
    {tags.map(tag => (
      <Tag key={tag} text={tag} />
    ))}
  </Container>
);

TagContainer.propTypes = {
  tags: PropTypes.arrayOf(PropTypes.string.isRequired).isRequired,
};

export default TagContainer;
