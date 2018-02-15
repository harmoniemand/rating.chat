const assert = require('chai').assert;
const messages = require("../messages");


const votes = {
    "user1": {
        name: "Leandro",
        selection: {
            "döner": 0.25,
            "salami": 0.5,
            "pilze": 0.25
        }
    },
    "user2": {
        name: "Joni",
        selection: {
            "salami": 0.25,
            "pilze": 0.25
        }
    },
    "user3": {
        name: "Vale",
        selection: {
            "salami": 0.25,
            "pilze": 0.25,
            "schinken": 1
        }
    },
    "user4": {
        name: "Adrian"
    },
    "user5": {
        name: "Adrian",
        selection: {}
    }
};



describe("createVoteStatus", () => {
    it("should create status message", () => {
        const result = messages.createUserOverview(votes);
        assert.equal(result, "Leandro möchte viertel döner, halbe salami und viertel pilze, " +
            "Joni möchte viertel salami und viertel pilze und " +
            "Vale möchte viertel salami, viertel pilze und ganze schinken");
    });
    it("should sum selections", () => {
        const result = messages.sumSelections(votes);
        assert.equal(result["pilze"], 0.75);
        assert.equal(result["salami"], 1);
        assert.equal(result["döner"], 0.25);
        assert.equal(result["schinken"], 1);

    });
    it("should create sum overiew", () => {
        const sums = messages.sumSelections(votes);
        const result = messages.createSumOverview(sums);

        assert.equal(result, "Zu bestellen wären: \n0.25 döner\n1 salami\n0.75 pilze\n1 schinken\nInsgesamt also min. 3 Pizzen");

    });
});