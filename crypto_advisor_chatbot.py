"""
Week 1 Assignment: Cryptocurrency Advisor Chatbot
Theme: "Your First AI-Powered Financial Sidekick!" 🌟
Author: Brian Ambeyi
Date: July 3, 2025
"""

import time
import random

class CryptoBuddy:
    """
    CryptoBuddy - Your AI-Powered Cryptocurrency Advisor Chatbot
    A rule-based chatbot that analyzes cryptocurrency data and provides 
    investment advice based on profitability and sustainability.
    """
    
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
                "current_price": "$67,500",
                "description": "The original cryptocurrency, digital gold standard"
            },
            "Ethereum": {
                "symbol": "ETH", 
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "current_price": "$3,800",
                "description": "Smart contract platform powering DeFi and NFTs"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
                "current_price": "$0.45",
                "description": "Proof-of-stake blockchain focused on sustainability"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10,
                "current_price": "$145",
                "description": "High-speed blockchain for DApps and crypto apps"
            },
            "Polygon": {
                "symbol": "MATIC",
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 9/10,
                "current_price": "$0.85",
                "description": "Ethereum scaling solution with eco-friendly approach"
            }
        }
        
        self.greetings = [
            f"Hey there! I'm {self.name}! 🚀 Let's find you a green and growing crypto!",
            f"Welcome to {self.name}! Your friendly crypto advisor is here! 💎",
            f"Hi! {self.name} here, ready to help you navigate the crypto world! 🌟"
        ]
        
        self.farewell_messages = [
            "Happy investing! Remember: crypto is risky—always do your own research! 📈💰",
            "See you later! May your portfolio be green and your gains be plenty! 🍀",
            "Goodbye! Stay safe in the crypto world and diversify your investments! 👋"
        ]

    def display_intro(self):
        """Display chatbot introduction and personality"""
        print("=" * 60)
        print("🤖 CRYPTOBUDDY - YOUR AI CRYPTO ADVISOR 🤖")
        print("=" * 60)
        print(random.choice(self.greetings))
        print("\n📊 I can help you with:")
        print("• Finding trending cryptocurrencies")
        print("• Sustainable crypto recommendations") 
        print("• Profitability analysis")
        print("• General crypto advice")
        print("\n⚠️  DISCLAIMER: Crypto investing is risky. Always do your own research!")
        print("-" * 60)

    def analyze_profitability(self):
        """Analyze and recommend based on profitability"""
        profitable_coins = []
        
        for coin, data in self.crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
                profitable_coins.append((coin, data))
        
        if profitable_coins:
            print("\n💰 PROFITABILITY ANALYSIS:")
            print("Based on price trends and market cap, here are my top picks:")
            
            for i, (coin, data) in enumerate(profitable_coins[:3], 1):
                print(f"\n{i}. {coin} ({data['symbol']})")
                print(f"   📈 Price: {data['current_price']}")
                print(f"   📊 Trend: {data['price_trend'].title()}")
                print(f"   🏪 Market Cap: {data['market_cap'].title()}")
                print(f"   💡 Why: {data['description']}")
        else:
            print("No strongly profitable coins found in current market conditions.")

    def analyze_sustainability(self):
        """Analyze and recommend based on sustainability"""
        sustainable_coins = []
        
        for coin, data in self.crypto_db.items():
            if data["energy_use"] == "low" and data["sustainability_score"] >= 0.7:
                sustainable_coins.append((coin, data))
        
        # Sort by sustainability score
        sustainable_coins.sort(key=lambda x: x[1]["sustainability_score"], reverse=True)
        
        if sustainable_coins:
            print("\n🌱 SUSTAINABILITY ANALYSIS:")
            print("Eco-friendly cryptos for the environmentally conscious investor:")
            
            for i, (coin, data) in enumerate(sustainable_coins[:3], 1):
                score_out_of_10 = int(data["sustainability_score"] * 10)
                print(f"\n{i}. {coin} ({data['symbol']})")
                print(f"   🌍 Sustainability Score: {score_out_of_10}/10")
                print(f"   ⚡ Energy Use: {data['energy_use'].title()}")
                print(f"   📈 Price: {data['current_price']}")
                print(f"   💡 Why: {data['description']}")
        else:
            print("No highly sustainable coins found in database.")

    def get_best_overall_recommendation(self):
        """Get best overall recommendation balancing profitability and sustainability"""
        print("\n🎯 CRYPTOBUDDY'S TOP RECOMMENDATION:")
        
        best_coin = None
        best_score = 0
        
        for coin, data in self.crypto_db.items():
            # Calculate combined score
            profit_score = 0
            if data["price_trend"] == "rising":
                profit_score += 3
            if data["market_cap"] == "high":
                profit_score += 2
            elif data["market_cap"] == "medium":
                profit_score += 1
                
            sustainability_multiplier = data["sustainability_score"]
            combined_score = profit_score * (1 + sustainability_multiplier)
            
            if combined_score > best_score:
                best_score = combined_score
                best_coin = (coin, data)
        
        if best_coin:
            coin, data = best_coin
            score_out_of_10 = int(data["sustainability_score"] * 10)
            print(f"\n🏆 My top pick is: {coin} ({data['symbol']})")
            print(f"📈 Current Price: {data['current_price']}")
            print(f"📊 Trend: {data['price_trend'].title()}")
            print(f"🌍 Sustainability: {score_out_of_10}/10")
            print(f"💡 Why this coin: {data['description']}")
            print(f"\n✨ {coin} offers the best balance of growth potential and sustainability!")

    def show_all_cryptos(self):
        """Display all available cryptocurrencies"""
        print("\n📋 ALL AVAILABLE CRYPTOCURRENCIES:")
        print("-" * 50)
        
        for coin, data in self.crypto_db.items():
            score_out_of_10 = int(data["sustainability_score"] * 10)
            print(f"\n💎 {coin} ({data['symbol']})")
            print(f"   💰 Price: {data['current_price']}")
            print(f"   📈 Trend: {data['price_trend'].title()}")
            print(f"   🏪 Market Cap: {data['market_cap'].title()}")
            print(f"   ⚡ Energy Use: {data['energy_use'].title()}")
            print(f"   🌍 Sustainability: {score_out_of_10}/10")

    def process_user_query(self, query):
        """Process user input and provide appropriate response"""
        query_lower = query.lower()
        
        # Sustainability-related queries
        if any(word in query_lower for word in ["sustainable", "eco", "environment", "green", "energy"]):
            self.analyze_sustainability()
            
        # Profitability-related queries  
        elif any(word in query_lower for word in ["profit", "trending", "rising", "money", "gain", "growth"]):
            self.analyze_profitability()
            
        # Best recommendation queries
        elif any(word in query_lower for word in ["best", "recommend", "should", "buy", "invest", "top"]):
            self.get_best_overall_recommendation()
            
        # List all cryptos
        elif any(word in query_lower for word in ["all", "list", "show", "available", "options"]):
            self.show_all_cryptos()
            
        # Specific coin queries
        elif any(coin.lower() in query_lower for coin in self.crypto_db.keys()):
            for coin, data in self.crypto_db.items():
                if coin.lower() in query_lower:
                    score_out_of_10 = int(data["sustainability_score"] * 10)
                    print(f"\n🔍 {coin} ({data['symbol']}) Analysis:")
                    print(f"💰 Current Price: {data['current_price']}")
                    print(f"📈 Price Trend: {data['price_trend'].title()}")
                    print(f"🏪 Market Cap: {data['market_cap'].title()}")
                    print(f"⚡ Energy Use: {data['energy_use'].title()}")
                    print(f"🌍 Sustainability Score: {score_out_of_10}/10")
                    print(f"💡 About: {data['description']}")
                    break
                    
        # Help queries
        elif any(word in query_lower for word in ["help", "what", "how", "can you"]):
            print("\n🤖 I can help you with:")
            print("• 'What's trending?' - Show profitable cryptocurrencies")
            print("• 'Most sustainable crypto?' - Show eco-friendly options")
            print("• 'Best recommendation?' - My top balanced pick")
            print("• 'Show all cryptos' - List all available options")
            print("• Ask about specific coins like 'Tell me about Bitcoin'")
            
        else:
            responses = [
                "🤔 I'm not sure about that. Try asking about trending cryptos or sustainable options!",
                "💭 Hmm, could you rephrase that? I specialize in crypto advice!",
                "🔄 Let me help you better - ask about profitability, sustainability, or specific coins!"
            ]
            print(f"\n{random.choice(responses)}")

    def run_chatbot(self):
        """Main chatbot conversation loop"""
        self.display_intro()
        
        while True:
            try:
                print("\n" + "─" * 40)
                user_input = input("🗣️  Ask me anything about crypto (or 'quit' to exit): ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"\n{random.choice(self.farewell_messages)}")
                    break
                
                if user_input:
                    print("\n💭 Analyzing your request...")
                    time.sleep(1)  # Add slight delay for realism
                    self.process_user_query(user_input)
                else:
                    print("Please enter a question or type 'quit' to exit.")
                    
            except KeyboardInterrupt:
                print(f"\n\n{random.choice(self.farewell_messages)}")
                break
            except Exception as e:
                print(f"😅 Oops! Something went wrong: {e}")
                print("Please try again!")

def main():
    """Main function to run the chatbot"""
    print("🚀 Initializing CryptoBuddy...")
    time.sleep(1)
    
    chatbot = CryptoBuddy()
    chatbot.run_chatbot()

if __name__ == "__main__":
    main()
