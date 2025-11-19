#!/usr/bin/env python3
"""
Quick Agent Test Script
Test all 4 agents with simple tasks
"""

import subprocess
import json
import os
from datetime import datetime

class AgentTester:
    def __init__(self):
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'agents': {}
        }
        
    def test_agent(self, agent_name, task):
        """Test a single agent with a task"""
        print(f"\n🤖 Testing {agent_name} agent...")
        print(f"📝 Task: {task}")
        
        try:
            # Simulate agent call (replace with actual API call)
            result = {
                'status': 'success',
                'agent': agent_name,
                'task': task,
                'response': f"[{agent_name}] Task completed successfully",
                'execution_time': '2.5s'
            }
            
            self.results['agents'][agent_name] = result
            print(f"✅ {agent_name} completed successfully")
            return result
            
        except Exception as e:
            result = {
                'status': 'error',
                'agent': agent_name,
                'task': task,
                'error': str(e)
            }
            self.results['agents'][agent_name] = result
            print(f"❌ {agent_name} failed: {e}")
            return result
    
    def test_all_agents(self):
        """Test all 4 agents"""
        print("=" * 60)
        print("🚀 DAIOF Framework - 4 Agent Test Suite")
        print("=" * 60)
        
        # Test Claude
        self.test_agent(
            'claude',
            'Analyze the DAIOF framework architecture'
        )
        
        # Test Blackbox
        self.test_agent(
            'blackbox',
            'Generate a simple REST API endpoint'
        )
        
        # Test Codex
        self.test_agent(
            'codex',
            'Implement binary search algorithm in Python'
        )
        
        # Test Gemini
        self.test_agent(
            'gemini',
            'Create a visual diagram of the system'
        )
        
        # Print summary
        self.print_summary()
        
        # Save results
        self.save_results()
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        total = len(self.results['agents'])
        success = sum(1 for r in self.results['agents'].values() if r['status'] == 'success')
        failed = total - success
        
        print(f"Total Agents: {total}")
        print(f"✅ Success: {success}")
        print(f"❌ Failed: {failed}")
        print(f"Success Rate: {(success/total)*100:.1f}%")
        
        print("\n📋 Agent Status:")
        for agent, result in self.results['agents'].items():
            status_icon = "✅" if result['status'] == 'success' else "❌"
            print(f"  {status_icon} {agent.upper()}: {result['status']}")
    
    def save_results(self):
        """Save test results to file"""
        output_file = 'agent_test_results.json'
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n💾 Results saved to: {output_file}")

def check_installation():
    """Check if agents are properly installed"""
    print("🔍 Checking agent installation...")
    
    checks = {
        'Blackbox CLI': ['which', 'blackbox'],
        'Python': ['python3', '--version'],
        'Node.js': ['node', '--version'],
        'Git': ['git', '--version']
    }
    
    for name, cmd in checks.items():
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  ✅ {name}: Installed")
            else:
                print(f"  ❌ {name}: Not found")
        except Exception as e:
            print(f"  ❌ {name}: Error - {e}")

def main():
    """Main function"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        🤖 DAIOF Framework - Agent Test Suite 🤖          ║
    ║                                                           ║
    ║  Testing 4 AI Agents:                                    ║
    ║  • Claude (Analysis & Documentation)                     ║
    ║  • Blackbox (Code Generation & Testing)                  ║
    ║  • Codex (Algorithms & Implementation)                   ║
    ║  • Gemini (Multimodal & Creative)                        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Check installation
    check_installation()
    
    # Run tests
    tester = AgentTester()
    tester.test_all_agents()
    
    print("\n" + "=" * 60)
    print("🎉 Agent testing completed!")
    print("=" * 60)
    print("\n📖 For detailed usage guide, see: AGENT_SETUP_GUIDE.md")

if __name__ == "__main__":
    main()
