const bcryptjs = require('bcryptjs');

const hashPassword = async function(password) {
    const saltRounds = 10;
    const hashPass = await bcryptjs.hash(password, saltRounds);
    return hashPass;
};

const comparePassword = async function(password, hashPass) {
    return bcryptjs.compare(password, hashPass);
};
 
module.exports = { hashPassword, comparePassword };
