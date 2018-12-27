import PropTypes from 'prop-types';
import styled from 'react-emotion';

import colours from '../constants/colours';

const TagContainerB = styled.button`
  margin: 0 3px;
  font-size: 100%;
  font-family: inherit;
  padding: 0;
  position: relative;

  display: inline-block;
  border: none;
  text-decoration: none;
  font-size: 1rem;
  cursor: pointer;
  text-align: center;
  -webkit-appearance: none;
  -moz-appearance: none;

  transition: color 250ms ease-in-out, transform 150ms ease;

  &:hover,
  &:focus {
    // background: ${colours.grey};
    color: ${colours.white};
  }

  &:focus {
    // outline: 1px solid #fff;
    // outline-offset: -4px;
  }

  &:active {
    transform: scale(0.99);
  }
`;

const TagContainer = styled.div`
  display: flex;
  height: 34px;
`;

const TagHead = styled.div`
  background-color: ${colours.yellowDark};
  width: 20px;
  height: 100%;
  clip-path: polygon(
    0 30% /* left top */,
    100% 0 /* right top */,
    100% 100% /* right bottom */,
    0 70% /* left bottom */
  );
  display: flex;
  align-items: center;

  transition: background 250ms ease-in-out;

  button:focus,
  button:hover & {
    background-color: ${colours.grey};
  }
`;

/* const Rope = styled.div`
  position: absolute;
  margin-top: 5px;
  margin-right: 5px;
  // padding-left: -20px;
  // overflow:
  // top: 15px;
  width: 20px;
  height: 20px;
  background: no-repeat center/80%
    url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAVUlEQVQoU2NkIBIw4lPXlar9HyRfNvsqI06FIEUgBSCFIDZWhciKUBTCrIA5A9kkuNXoumEmwBTANDNiswZmIrJH4Y4FSSL7Ej004J7B5gQME4kJcwCTkjQ9M8tDXgAAAABJRU5ErkJggg==);
`; */

const Circle = styled.div`
  height: 5px;
  width: 5px;
  margin-left: 5px;
  border-radius: 50%;
  background-color: ${colours.white};
  border: solid 1px red;
`;

const TagContent = styled.div`
  background-color: ${colours.yellowDark};
  padding-right: 10px;
  display: flex;
  font-size: 12px;
  font-weight: bold;
  min-width: 40px;
  justify-content: center;
  align-items: center;

  transition: background 250ms ease-in-out;

  button:focus,
  button:hover & {
    background-color: ${colours.grey};
  }
`;

const Img = styled.img`
  position: absolute;
  top: 15px;
  left: -10px;
`;

const Tag = ({ text }) => (
  <TagContainerB>
    <TagContainer>
      <TagHead>
        {/* <Rope /> */}
        <Circle />
      </TagHead>
      <TagContent>{text}</TagContent>
    </TagContainer>
    <Img height="30px" width="40px" src="../assets/rope.svg" alt="rope" />
  </TagContainerB>
);

Tag.propTypes = {
  text: PropTypes.string.isRequired,
};

export default Tag;
