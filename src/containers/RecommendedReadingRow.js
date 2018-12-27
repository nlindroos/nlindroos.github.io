import PropTypes from 'prop-types';
import styled from 'react-emotion';
import { Typography } from '@material-ui/core';

import ResourceIcon from '../components/ResourceIcon';
import TagContainer from './TagContainer';

const RowContainer = styled.div`
  margin: 20px;
  display: flex;
  flex-direction: column;
`;

const TitleRow = styled.div`
  display: flex;
  align-items: center;
`;

const RecommendedReadingRow = ({ resource }) => (
  <RowContainer>
    <TitleRow>
      <ResourceIcon type={resource.type} />
      <Typography variant="h6">{resource.title}</Typography>
    </TitleRow>
    {!!resource.description && <Typography variant="subtitle2">{resource.description}</Typography>}

    <TagContainer tags={resource.tags} />
  </RowContainer>
);

RecommendedReadingRow.propTypes = {
  resource: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string,
    tags: PropTypes.arrayOf(PropTypes.string),
    type: PropTypes.string.isRequired,
  }).isRequired,
};

export default RecommendedReadingRow;
